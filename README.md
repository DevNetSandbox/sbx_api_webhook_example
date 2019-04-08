# About this App

The purpose of this app is to provide a simple way to receive the data pushed by the webhook in the sandbox API.  The code in this repo will start a simple flask server on port 8080 that will listen for and print any incoming HTTP requests it receives.

# To use this App

Before you start, make sure you have the following prerequesites installed;

## Prerequisites:
- Docker: for more infomration see [the docker install docs](https://docs.docker.com/install)
- Ngrok: you'll need an externally facing address for the webhook to point to, and ngrok gives you a super easy way to do that!  You can [install it here](https://ngrok.com/download)

Once you've got Docker and ngrok set up, you're ready to run the app!

You'll need two terminal windows for this: one for docker and one for ngrok.  In one window, run the following commands to start the app:

``` 
git clone https://github.com/DevNetSandbox/sbx_api_webhook_example.git
cd sbx_api_webhook_example
docker-compose up
```

This will create a docker container running the application on port 8080.  You should be able to see the POST request come in if you run the following command:

```  
curl -X POST localhost:8080 -d '{"msg":"hello world!"}' 
```

However, at this point you'll only be able to hit the endpoint over localhost.  To expose our endpoint to the internet, run the following command in your second terminal windows:

``` 
ngrok http 8080
```

You'll receive an endpoint that looks something like this:

```
http://xxxxxxxx.ngrok.io -> localhost:8080
```
This means that the ngrok name is now pointing to your local server.  Copy the ``` http://xxxxxxxx.ngrok.io``` address and use it as the target for your webhook!

As the requests come in from the sandbox API, you'll be able to see the data in the Docker window.
