import base64
import json
from io import BytesIO

from deepface import DeepFace
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from textblob import TextBlob

from guider.utils import MoonDream, Bart
from home.models import Post, VerificationImage, Profile


@login_required
def index(request):
    posts = Post.objects.all()
    verified = request.session.get('verified', False)
    return render(request, 'home/index.html', context={"posts": posts, "verified": verified})


@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('message')
        image = request.FILES.get('image')
        verified = request.session.get('verified', False)

        if not content:
            return redirect('home', permanent=True)

        blob = TextBlob(content)
        post = Post.objects.create(
            content=content,
            author=request.user,
            image=image,
            sentiment=blob.sentiment.polarity,
            verified=verified
        )

        if post.image:
            post.caption = MoonDream().generate(post.image.path)
            post.save()

    return redirect('home', permanent=True)


@login_required
def verify_face(request):
    if request.method == 'POST':
        # Parse the JSON received from the frontend
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        image_data = json_data['image_data']
        extension, img_str = image_data.split(';base64,')
        image_bytes = base64.b64decode(img_str)

        verification_image = VerificationImage.objects.create(user=request.user)
        verification_image.image.save('temp.jpg', BytesIO(image_bytes))

        profile = request.user.profile

        if not profile.image:
            return JsonResponse({'message': 'Profile image not found.'}, status=400)

        # Load the known face image from the user's profile
        try:
            # Using DeepFace to verify the face
            verification_result = DeepFace.verify(img1_path=profile.image.path,
                                                  img2_path=verification_image.image.path)

            if verification_result["verified"]:
                # Verify the user and set a session token
                request.session['verified'] = True  # You can set a more complex session state or token
                return JsonResponse({'message': 'User verified successfully.'}, status=200)
            else:
                return JsonResponse({'message': 'Verification failed.'}, status=401)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request'}, status=400)


@login_required
def update_profile(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        profile = Profile.objects.get_or_create(user=request.user)[0]
        profile.image = image
        profile.save()

    return redirect('home', permanent=True)


def summary(request):
    posts = Post.objects.all()
    post_texts = ""

    for post in posts:
        post_texts += f"@{post.author.username} posted:\n{post.content}\n"

    summary_text = Bart().generate_summary(post_texts)

    return render(request, 'home/summary.html', context={"summary": summary_text})
