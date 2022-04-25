import requests

END_POINT_URL  = 'https://api.notion.com/v1/'

def getPageContent(page_id):

    r = requests.get(END_POINT_URL + 'blocks/' + page_id + '/children', headers= { "Authorization" : "secret_wjwAXnpD44OnFH5FGj5YNWEy5inju4tuHiojenFeYj4", "Notion-Version" : "2021-05-13"})    
    content = r.json()

    if content["object"] == "error":
        return None
    
    text_content = ""
    for block in content["results"]:
        t = block["type"]

        if "text" not in block[t]:
            continue
        txts = block[t]["text"]
        for txt in txts:
            text_content += txt["plain_text"] + " \n"

    return text_content
    