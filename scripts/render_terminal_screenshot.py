import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal_image(output_path, title, lines_data):
    # Setup dimensions
    font_size = 18
    line_height = 26
    padding_x = 24
    padding_y = 18
    header_height = 42

    # Try to load Windows font
    font_path = r"C:\Windows\Fonts\consola.ttf"
    if not os.path.exists(font_path):
        font_path = r"C:\Windows\Fonts\arial.ttf"
    
    try:
        font = ImageFont.truetype(font_path, font_size)
        title_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 14)
    except:
        font = ImageFont.load_default()
        title_font = font

    # Calculate required height and width
    content_height = len(lines_data) * line_height + padding_y * 2
    total_height = header_height + content_height
    total_width = 1000

    # Create image
    # Background: dark slate / terminal dark
    bg_color = (18, 22, 30)
    header_color = (28, 33, 44)
    border_color = (45, 52, 68)

    img = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw rounded rect or bordered window
    draw.rounded_rectangle(
        [(0, 0), (total_width - 1, total_height - 1)],
        radius=10,
        fill=bg_color,
        outline=border_color,
        width=1
    )

    # Header bar
    draw.rounded_rectangle(
        [(0, 0), (total_width - 1, header_height)],
        radius=10,
        fill=header_color
    )
    # Fill bottom part of header to make flat edge with body
    draw.rectangle([(0, header_height - 10), (total_width - 1, header_height)], fill=header_color)
    draw.line([(0, header_height), (total_width - 1, header_height)], fill=border_color, width=1)

    # Window control buttons (macOS style or Windows style)
    # 3 colored dots
    dot_radius = 6
    dot_y = header_height // 2
    draw.ellipse([(20 - dot_radius, dot_y - dot_radius), (20 + dot_radius, dot_y + dot_radius)], fill=(255, 95, 86))
    draw.ellipse([(40 - dot_radius, dot_y - dot_radius), (40 + dot_radius, dot_y + dot_radius)], fill=(255, 189, 46))
    draw.ellipse([(60 - dot_radius, dot_y - dot_radius), (60 + dot_radius, dot_y + dot_radius)], fill=(39, 201, 63))

    # Window title centered
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((total_width - title_w) // 2, (header_height - (title_bbox[3] - title_bbox[1])) // 2), title, font=title_font, fill=(180, 190, 205))

    # Render lines
    y = header_height + padding_y
    for line_segments in lines_data:
        x = padding_x
        for text, color in line_segments:
            draw.text((x, y), text, font=font, fill=color)
            bbox = draw.textbbox((x, y), text, font=font)
            x = bbox[2]
        y += line_height

    # Ensure target directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated {output_path}")

# Line color palettes
C_PROMPT = (97, 175, 239)      # Blue
C_PATH = (229, 192, 123)       # Yellow/Gold
C_TEXT = (220, 225, 235)       # Off-white
C_MUTED = (120, 130, 150)      # Gray
C_GREEN = (152, 195, 121)      # Green
C_YELLOW = (229, 192, 123)     # Yellow
C_RED = (224, 108, 117)        # Red
C_MAGENTA = (198, 120, 221)    # Magenta / Purple
C_CYAN = (86, 182, 194)        # Cyan
C_BRANCH = (97, 175, 239)      # Branch name blue

screenshot_lines = [
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("git status", C_TEXT)],
    [("On branch ", C_TEXT), ("feature-api", C_GREEN)],
    [("nothing to commit, working tree clean", C_MUTED)],
    [("", C_TEXT)],
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("git log --graph --oneline --decorate --all", C_TEXT)],
    [("* ", C_YELLOW), ("3a76b3f ", C_CYAN), ("(HEAD -> ", C_MUTED), ("feature-api", C_GREEN), (") ", C_MUTED), ("feat: enable debug", C_TEXT)],
    [("* ", C_YELLOW), ("6a7dfef ", C_CYAN), ("feat: change port", C_TEXT)],
    [("* ", C_YELLOW), ("351293b ", C_CYAN), ("(", C_MUTED), ("main", C_YELLOW), (") ", C_MUTED), ("add env config", C_TEXT)],
    [("* ", C_YELLOW), ("32af75b ", C_CYAN), ("update port on main", C_TEXT)],
    [("* ", C_YELLOW), ("d604782 ", C_CYAN), ("init config", C_TEXT)],
    [("", C_TEXT)],
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("Get-Content config.json", C_TEXT)],
    [("{", C_TEXT)],
    [('  "port": ', C_TEXT), ("9000", C_YELLOW), (",", C_TEXT)],
    [('  "debug": ', C_TEXT), ("true", C_GREEN), (",", C_TEXT)],
    [('  "env": ', C_TEXT), ('"production"', C_YELLOW)],
    [("}", C_TEXT)],
    [("", C_TEXT)],
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("█", C_PROMPT)],
]

# Generate main image
render_terminal_image(
    "homework/session_05/ex3/assets/git_log_rebase.png",
    "PowerShell - Git Rebase Finished Linear Graph",
    screenshot_lines
)

# Also copy to root assets
render_terminal_image(
    "assets/git_log_rebase.png",
    "PowerShell - Git Rebase Finished Linear Graph",
    screenshot_lines
)

# Also generate a second image showing the step-by-step conflict resolution process!
conflict_lines = [
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("git checkout feature-api; git rebase main", C_TEXT)],
    [("Auto-merging config.json", C_TEXT)],
    [("CONFLICT (content): Merge conflict in config.json", C_RED)],
    [("error: could not apply a0537cb... feat: change port", C_RED)],
    [("hint: Resolve all conflicts manually, mark them as resolved with ...", C_MUTED)],
    [("", C_TEXT)],
    [("--- [Chặng 1: Xử lý conflict port: 9000 vs 8081] ---", C_YELLOW)],
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("git add config.json; git rebase --continue", C_TEXT)],
    [("[detached HEAD 6a7dfef] feat: change port", C_CYAN)],
    [("Auto-merging config.json", C_TEXT)],
    [("CONFLICT (content): Merge conflict in config.json", C_RED)],
    [("error: could not apply 081a323... feat: enable debug", C_RED)],
    [("", C_TEXT)],
    [("--- [Chặng 2: Xử lý conflict debug: true vs false & env: production] ---", C_YELLOW)],
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("git add config.json; git rebase --continue", C_TEXT)],
    [("[detached HEAD 3a76b3f] feat: enable debug", C_CYAN)],
    [("Successfully rebased and updated refs/heads/feature-api.", C_GREEN)],
    [("", C_TEXT)],
    [("PS D:\\IT209\\Session5_b3> ", C_PROMPT), ("█", C_PROMPT)],
]

render_terminal_image(
    "homework/session_05/ex3/assets/git_rebase_conflicts.png",
    "PowerShell - Step-by-Step Conflict Resolution in Rebase",
    conflict_lines
)
render_terminal_image(
    "assets/git_rebase_conflicts.png",
    "PowerShell - Step-by-Step Conflict Resolution in Rebase",
    conflict_lines
)
