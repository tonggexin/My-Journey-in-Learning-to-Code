import MyUI
import pygame

# Load music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# Initialize app
WIDTH, HEIGHT = 800, 600
app = MyUI.App((WIDTH, HEIGHT))
pygame.display.set_caption("Simple MyUI Demo")

# Load plugins from folder
plugin_wrappers = MyUI.load_plugins_from("plugins")

# Handle plugins before loading
plugin_group = MyUI.plugins.create_dict(MyUI.plugins.get_plugin_group(plugin_wrappers, "plugin"))
entry = plugin_group.get("entry")
print(entry.plugin_name) # Plugin name
print(entry.entry_name) # Entry name
print(entry.name) # Name is "plugin-entry", each plugin has seperate entries, each has seperate functions and different wrappers.

# Create a reload method
def reload_plugins():
    global plugin_wrappers
    plugin_wrappers = MyUI.load_plugins_from("plugins")
    app.reload(plugin_wrappers)

# Load fonts
fonts = MyUI.FontScheme(
    small1=pygame.font.SysFont("consolas", 15)
)

# Create a button
button = MyUI.PushButton(
    text="Reload!",
    font=fonts.small1,
    pos=(50, 50),
    size=(100, 30),
    color=(50, 50, 150),
    hover_color=(70, 70, 170),
    callback=reload_plugins
)

# Create a surface
surf = MyUI.Surface(
    pos=(100, 50),
    size=(200, 200),
    background_color=(200, 200, 250),
    border_color=(225, 225, 255),
    border_width=2,
    border_radius=5
)

# Add UI elements to the top layer
surf.add_handler(button.render, button.handle_event)
app.add_top(surf.render, surf.handle_event)

# Attach plugins
app.load_plugins(plugin_wrappers)

# Run the app
app.run()