from PIL import Image 
from IPython.display import display 
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%


back = [
    "pre_reveal_ticket",
    "pre_revealticket2"
] 
back_weights = [45, 55]

none = [
    "none"
]
none_weights = [100]

back_files = {
    "pre_reveal_ticket": "pre_reveal_ticket",
    "pre_revealticket2": "pre_revealticket2"
}

none_files = {
    "none": "NONE"
}

## Generate Traits
TOTAL_IMAGES = 10 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Back"] = random.choices(back, back_weights)[0]
    new_image ["None"] = random.choices(none, none_weights)[0]


    # if new_image in all_images:
    #     return create_new_image()
    # else:
    #     return new_image
    return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

# print("Are all images unique?", all_images_unique(all_images))

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

# print(all_images)

# Get Trait Counts
# acc_count = {}
# for item in acc:
#     acc_count[item] = 0
    
# body_count = {}
# for item in body:
#     body_count[item] = 0

# clothes_count = {}
# for item in clothes:
#     clothes_count[item] = 0

# eye_count = {}
# for item in eye:
#     eye_count[item] = 0

# hand_count = {}
# for item in hand:
#     hand_count[item] = 0

# hat_count = {}
# for item in hat:
#     hat_count[item] = 0

# legs_count = {}
# for item in legs:
#     legs_count[item] = 0 

# mouth_count = {}
# for item in mouth:
#     mouth_count[item] = 0
    
# mouth_count = {}
# for item in mouth:
#     mouth_count[item] = 0

# for image in all_images:
#     acc_count[image["Acc"]] += 1
#     body_count[image["Body"]] += 1
#     clothes_count[image["Clothes"]] += 1
#     eye_count[image["Eye"]] += 1
#     hand_count[image["Hand"]] += 1
#     hat_count[image["Hat"]] += 1
#     legs_count[image["Legs"]] += 1
#     mouth_count[image["Mouth"]] += 1

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
for item in all_images:

   
    im1 = Image.open(f'./trait-layers/pre_reveal/{back_files[item["Back"]]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/none/{none_files[item["None"]]}.png').convert('RGBA')

    #Create each composite 
    com1 = Image.alpha_composite(im1, im2)

    #Convert to RGB
    rgb_im = com1.convert('RGBA')
        

    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
	
#### Generate Metadata for each Image    
f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "BreadWinner"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id)
    }   

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()