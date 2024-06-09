from playsound import playsound # use an alternative
# from soundsmake import states, dishes
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Lakshadweep", "Delhi", "Puducherry"]

# Corresponding list of dishes
dishes = [
    ("Hyderabadi Biryani", "Pesarattu", "Gongura Pickle"),  # Andhra Pradesh
    ("Apong", "Momos", "Thukpa"),  # Arunachal Pradesh
    ("Masor Tenga", "Aloo Pitika", "Pitha"),  # Assam
    ("Litti Chokha", "Sattu Paratha", "Chaat"),  # Bihar
    ("Farra", "Chousela", "Kosra"),  # Chhattisgarh
    ("Sorpotel", "Vindaloo", "Bebinca"),  # Goa
    ("Dhokla", "Thepla", "Undhiyu"),  # Gujarat
    ("Chole Bhature", "Sarson Ka Saag", "Kachri ki Sabzi"),  # Haryana
    ("Dham", "Siddu", "Chha Gosht"),  # Himachal Pradesh
    ("Pitti", "Dhuska", "Chilka Roti"),  # Jharkhand
    ("Bisi Bele Bath", "Mysore Pak", "Neer Dosa"),  # Karnataka
    ("Appam", "Idiyappam", "Kerala Fish Curry"),  # Kerala
    ("Poha", "Bhutte Ka Kees", "Indori Poha"),  # Madhya Pradesh
    ("Vada Pav", "Pav Bhaji", "Misal Pav"),  # Maharashtra
    ("Chak-Hao Kheer", "Manipuri Fish Curry", "Eromba"),  # Manipur
    ("Jadoh", "Doh Khleh", "Pukhlein"),  # Meghalaya
    ("Bai", "Arsa Buhchiar", "Koat Pitha"),  # Mizoram
    ("Akini Chokibo", "Beej Roti", "Aikikando"),  # Nagaland
    ("Dahibara Aloodum", "Chhena Poda", "Chingudi Jhola"),  # Odisha
    ("Makki di Roti", "Sarson da Saag", "Amritsari Kulcha"),  # Punjab
    ("Dal Baati Churma", "Laal Maas", "Gatte ki Sabzi"),  # Rajasthan
    ("Phagshapa", "Sha Phaley", "Chhurpi Soup"),  # Sikkim
    ("Filter Coffee", "Chettinad Chicken", "Pongal"),  # Tamil Nadu
    ("Hyderabadi Biryani", "Mirchi Bajji", "Dum Pukht"),  # Telangana
    ("Bibikhatoon Aamba", "Moirangphee", "Eromba"),  # Tripura
    ("Tunday Kababi", "Aloo ki Sabzi", "Petha"),  # Uttar Pradesh
    ("Garhwali Cuisines", "Phaanu", "Kandalee Ka Saag"),  # Uttarakhand
    ("Rasgulla", "Macher Jhol", "Kolkata Biryani"),  # West Bengal
    ("Coconut Fish Curry", "Prawns Fry", "Tuna Thoran"),  # Andaman and Nicobar Islands
    ("Chole Bhature", "Sarson Da Saag", "Matar Paneer"),  # Chandigarh
    ("Dhokla", "Fafda Jalebi", "Bardoli Ki Khichdi"),  # Dadra and Nagar Haveli and Daman and Diu
    ("Tuna Thoran", "Kappa Meen Curry", "Pathiri"),  # Lakshadweep
    ("Chole Bhature", "Nihari", "Butter Chicken"),  # Delhi
    ("Masala Dosa", "Sambhar Vada", "Parotta"),  # Puducherry
]


sounds = []

# playing sounds

# important NOTE: the sounds should be played in order, first the info, then the foods 

def play(c_state):
    global sounds

    for x in range(3):
        current_sound = os.path.join("sounds/foods","dish"+c_state+str(x)+".mp3")
        sounds.append(current_sound)
    
    greeting_sound = os.path.join("sounds/info","greeting"+c_state+".mp3")

    # playeing the sounds

    playsound(sound=greeting_sound) # playing the info/greeting sound
    for sound in sounds: # after it finished playing info sounds, playing all 3 dishes sounds
        playsound(sound=sound)
    
    print(sounds)
    sounds = []