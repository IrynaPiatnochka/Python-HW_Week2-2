#Searching for keywords such as "good", "excellent", "bad", "poor", and "average". 
#Printing out each review with the keywords in uppercase so they stand out.

reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "Poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." ]    

def modified_reviews(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        for kwords in keywords:
            review = review.replace(kwords, kwords.upper())
            review = review.replace(kwords.title(), kwords.upper())
        print(review)

modified_reviews(reviews)


