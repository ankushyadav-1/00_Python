import requests

def fectch_random_user_freeapi():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()
    
    if data['success'] and "data" in data:
        user_data = data["data"]
        user_name = user_data['lodin']['username']
        contery = user_data['location']['country']
        return user_name, contery
    else:
        raise Exception("Failed to fetch user data")
    
    
    
def main():
    try:
        usernme, country = fectch_random_user_freeapi()
        print(f"Username: {usernme} \n Country: {country}")
    except Exception as e:
        print(str(e))


if __name__ =='__main__':
    main()        
        