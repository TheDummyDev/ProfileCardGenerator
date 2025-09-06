import svgwrite

def generate_profile_card(name, user_id, email):
    """
    Generates an SVG profile card.

    Args:
        name (str): The user's name.
        user_id (str): The user's ID.
        email (str): The user's email address.
    """
    width = 400
    height = 200
    dwg = svgwrite.Drawing('profile_card.svg', size=(width, height), profile='full')

    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=10, ry=10, fill='#f0f0f0'))

    # Profile picture placeholder
    dwg.add(dwg.circle(center=(70, 80), r=50, fill='#cccccc'))
    dwg.add(dwg.text('Avatar', insert=(45, 85), fill='#ffffff', style="font-size:16px; font-family:Arial"))


    # User Information
    dwg.add(dwg.text(name, insert=(150, 60), fill='#333333', style="font-size:24px; font-family:Arial; font-weight:bold"))
    dwg.add(dwg.text(f"ID: {user_id}", insert=(150, 90), fill='#666666', style="font-size:16px; font-family:Arial"))
    dwg.add(dwg.text(email, insert=(150, 120), fill='#666666', style="font-size:16px; font-family:Arial"))

    dwg.save()

if __name__ == '__main__':
    # Example usage:
    generate_profile_card("Jules", "12345", "jules@example.com")
    print("Profile card generated successfully as profile_card.svg")
