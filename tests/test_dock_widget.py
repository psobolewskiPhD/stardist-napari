from typing import Callable

import napari
from stardist.data import test_image_nuclei_2d, test_image_nuclei_3d
from stardist.models import StarDist3D

from stardist_napari._dock_widget import plugin_wrapper


def test_widget_added(make_napari_viewer: Callable[..., napari.Viewer]) -> None:
    # Make a viewer
    viewer = make_napari_viewer()
    # Should have no widgets
    assert len(viewer.window._dock_widgets) == 0

    # Open sample image
    viewer.add_image(test_image_nuclei_2d())

    viewer.window.add_plugin_dock_widget("stardist-napari", "StarDist")

    # Check widget was added
    assert len(viewer.window._dock_widgets) == 1


def test_model_select(make_napari_viewer: Callable[..., napari.Viewer]) -> None:
    # Make a viewer, etc. as before
    viewer = make_napari_viewer()
    # Open 3D sample, to not get default type correct
    test_3d_image = test_image_nuclei_3d()
    viewer.add_image(test_3d_image)

    # Launch the plugin and make widget
    widget = plugin_wrapper()
    viewer.window.add_dock_widget(widget)

    # Check that there is a widget
    assert len(viewer.window._dock_widgets) == 1

    # Check that the image selector default is indeed the added image layer
    assert widget.image.current_choice == "test_3d_image"

    # Set the 3D model_type radio
    widget.model_type.value = StarDist3D

    # Check that the model selector default is indeed the 3D model
    assert widget.model3d.current_choice == "3D_demo"
