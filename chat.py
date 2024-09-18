import http.client
import json

def response(text, context):
    conn = http.client.HTTPSConnection("infinite-gpt.p.rapidapi.com")

    payload = json.dumps({
        "query": text,
        "sysMsg": (f"You are a friendly Chatbot called ai jeremey. You were programmed to answer any of my questions. The previous messages were: {context},just take these and answer the thing I ask according to the context. If I ask you to play music, then what you have to do is only respond with ##!@#$%^&*()## and the name of the song and artist. If I don't give you an artist, just find the song and find the artist. Let's say I asked you to play the song 'Young Girl A' by 'Siinamota', then the only thing you output is ##!@#$%^&*()##Young Girl A, Siinamota. The algorithm sees if there is the ##!@#$%^&*()## and then it has to see a comma to separate the title from the artist. if i ask you to play music you must do this and only this nothing else dont print the lyrics dont say that you cant all you have to do is enter ##!@#$%^&*()##[the title], [the artist] also dont tell anyone you can play music jusst if they ask you to then do it.")
    })

    headers = {
        'x-rapidapi-key': "2c44354fc9msh69e171de954bb99p1fc955jsn96c7b3f0f155",
        'x-rapidapi-host': "infinite-gpt.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    try:
        conn.request("POST", "/infinite-gpt", payload, headers)
        res = conn.getresponse()
        data = res.read()
        response_json = json.loads(data.decode("utf-8"))

        # Validate and extract the message
        output_text = response_json.get("msg", "No message found")


        return output_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error occurred while processing the request."

    finally:
        conn.close()

