reviews = [ "This product is really good I'm impressed with its quality.", 
                  "The performance of this product is excellent Highly recommended!", 
                  "I had a bad experience with this product It didn't meet my expectations.", 
                  "Poor quality product Wouldn't recommend it to anyone.", 
                  "The product was average Nothing extraordinary about it." ]

#Developing a function that tallies the number of positive and negative words in each review.

def count_pos(reviews):
    positive_counter = 0
    positive = ["good", "excellent"]
    for review in reviews:
        
        print(review)
        for pos in review.split(" "):
            for word in positive:                
                if word == pos:
                    positive_counter +=1
    print(positive_counter)
            

count_pos(reviews)


reviews = [ "This product is really good I'm impressed with its quality.", 
                  "The performance of this product is excellent Highly recommended!", 
                  "I had a bad experience with this product It didn't meet my expectations.", 
                  "Poor quality product Wouldn't recommend it to anyone.", 
                  "The product was average Nothing extraordinary about it." ]

def count_neg(reviews):
    negative_counter = 0
    negative = ["poor", "bad", "average"]
    for review in reviews:
        print(review)
        for neg in review.split(" "):
            for word in negative:                
                if word == neg:
                    negative_counter +=1
    print(negative_counter)
          

count_neg(reviews)
