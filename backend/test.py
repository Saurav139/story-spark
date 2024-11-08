import chromadb
chroma_client = chromadb.Client()

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="my_collection")

documents=['The Stingray Prologue We finally arrived in Fiji after a', 'long boat ride. When we got to our “hut”. I', 'ran inside, then I unpacked my books and started reading.', 'Chapter 1 I’m bored “Appa I’m bored” I said “Then', 'how about you go outside and play with those kids?”', 'Appa asked. I talked to their parents yesterday and they', 'said that they came a few hours before us. “Okay”', 'I said. Chapter 2 Surfboard jump! I changed into my', 'swimsuit and went outside. Hey guys! I said. Hi! they', 'said. It had been a few days since I had', 'made friends with them, but today I was ready for', 'an adventure, “Suhana!” My friend called and broke me from', 'my thoughts. “Over here” I looked up and saw them', 'jumping from a surfboard. “Cool” I said “I’m coming: I', 'ran to the surfboard and jumped off it. It was', 'so fun. “Let’s go deeper,” my friend said. “Okay!” I', 'said. Then we made the biggest mistake. We went deeper.', 'Chapter 3 Let’s get out of here! “This is so', 'much fun,” I said. Let’s go deeper” So we went', 'deeper and deeper until it was as high as two', 'of me! Then we heard a motorboat. We looked and', 'saw a person calling us and yelling. “There are poisonous', 'stingrays here. Catch the hook and attach it to the', 'surfboard” So we did, then he went back to the', 'shore. It was a very fun ride. My parents were', 'so worried, but I still had a lot of fun.', 'Vasona Lake Vasona Lake is an amazing place. It might', 'not be the biggest lake, but it’s definitely a great', 'place to relax. First of all, Vasona Lake is a', 'great place to have a picnic, and when you sit', 'down you can see the calming water moving because of', 'the boaters. Then, if you look up you can see', 'hungry geese everywhere. Then, when it’s quiet you can hear', 'the soft hungry geese everywhere. Then, when it’s quiet you', 'can hear the soft ripples in the water. Also, the', 'air is super fresh and you can really smell it.', 'Furthermore, the lake has an ice cream truck that’s ice', 'cream is sweet and rich with flavor. In addition, there', 'is a great trail to Vasona where I always ride', 'my smooth, soft bike. To conclude Vasona lake is a', 'great place to use your senses and take some time', 'out of a troublesome day!']
ids = [f"doc_{i}" for i in range(len(documents))]      

#switch `add` to `upsert` to avoid adding the same documents every time
# collection.upsert(documents=documents,
#                   ids=ids
   
# )

results = collection.query(
    query_texts=["These bookas are awesome"], # Chroma will embed this for you
    n_results=3 # how many results to return
)

print(results)
