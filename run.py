import ollama
from thepipe.scraper import scrape_url
from thepipe.core import chunks_to_messages


def classify_video(surl):
    # scrape clean markdown
    # see https://github.com/pytube/pytube/issues/1750 if you get an error
    chunks = scrape_url(url=surl, local=True,  text_only=True)
    # we can do alot more than just the text, but for POC this will work
    sDoc = ""
    for chunk in chunks:
        sDoc += "\n".join(chunk.texts)
    print("Extracted audio transcribed")
    # print(sDoc)
    # call LLM with scraped chunks
    sprompt = open('prompt.md').read()
    # now we add our doc from the scrapper
    sprompt += sDoc
    print("Calling LLM")
    k = ollama.generate(model='llama3.1:70b', prompt=sprompt)
    return k['response']

# Run the FastAPI application
if __name__ == "__main__":

    surl = "https://www.youtube.com/watch?v=DUsj9SQYS1Y"
    k =  classify_video(surl)
    print(k)

    import IPython
    IPython.embed()
