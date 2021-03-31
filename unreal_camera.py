import unreal

# Editor & Selection

editor = unreal.EditorLevelLibrary()
selected_actors = editor.get_selected_level_actors()
camera = selected_actors[0]


def change_camera(x, y, z, field_of_view):

    # Adjust Camera Position
    new_transform = camera.get_actor_transform()
    new_transform.rotation.x = x
    new_transform.rotation.y = y
    new_transform.rotation.z = z

    camera.set_actor_transform(new_transform, True, True)

    # Adjust Camera Field
    camera.camera_component.set_editor_property('field_of_view', field_of_view)
    print('Current field_of_view = ', camera.camera_component.get_editor_property('field_of_view'))

    return True


def take_screenshot(height, width, screenshot_name):
    camera_view = camera.camera_component.get_camera_view(1)
    camera_location = camera_view.location
    unreal.AutomationLibrary.take_high_res_screenshot(int(height), int(width), screenshot_name, camera=camera,
                                                     mask_enabled=False, capture_hdr=True, delay=1.0)

    return True