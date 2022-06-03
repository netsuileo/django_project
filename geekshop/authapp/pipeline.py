import requests


def get_user_gender(user, response, *args, **kwargs):
    access_token = response["access_token"]
    vk_response = requests.get(
        f"https://api.vk.com/method/user.get?access_token={access_token}&v=5.92"
    )
    user.profile.about = vk_response.text
    user.profile.save()
    return {}
