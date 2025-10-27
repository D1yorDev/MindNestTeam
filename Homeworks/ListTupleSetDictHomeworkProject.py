# Project for learning List, Tuple, Set , Dictionary

contact = {
    "contact1": {
        "phone": "IPHONE",
        "hobbies": ["Reading", "Football", "Basketball"],
        "week": ("Monday", "Friday")

    },
    "contact2": {
        "phone": "Redmi",
        "hobbies": ["Reading", "Skybord", "Swimming"],
        "week": ("Tuesday", "Wednesday")

    },
    "contact3": {
        "phone": "Sumsung",
        "hobbies": ["Reading", "Jumping", "Coding"],
        "week": ("Sunday", "Saturday")

    }

}
contact4 = {
    "contact4": {
        "phone": "Vivo",
        "hobbies": ["Reading", "Dancing"],
        "week": ("Monday", "Sunday")
    }
}

contact.update(contact4)

contact['contact2']['hobbies'].append("Traveling")

unique_hobbies = {hobby for inner in contact.values() for hobby in inner.get("hobbies", [])}

print(f"All contacts: {contact}")
print(f"Unique Hobbies: {unique_hobbies}")