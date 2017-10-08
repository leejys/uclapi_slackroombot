import requests

def get_userdata(UCL_API_TOKEN, CLIENT_SECRET):
    params = {
      "token": UCL_API_TOKEN,
      "client_secret": CLIENT_SECRET
    }
    r = requests.get("https://uclapi.com/oauth/user/data", params=params)
    mydata = r.json()
    print(mydata)
    about_me = "Hello {} ({}), your department is the {}. UPI: {}, Email: {}. You are great!".format(
            mydata["full_name"],
            mydata["cn"],
            mydata["department"],
            mydata["upi"],
            mydata["email"]
            
        )
    return(about_me)

#get_userdata()
