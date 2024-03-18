from Slider import Slider 
from HSVColorPicker import HSVColorPicker

from pygame import Surface
from pygame import draw
from math import ceil

class HSVSlider(Slider):
    KNOB_THICKNESS = 1
    def __init__(self, position : tuple, size : tuple, hsvColorPicker : HSVColorPicker):
        sliderBG = HSVSlider.__makeSliderBG(size)
        knob     = HSVSlider.__makeKnob(size)
        super().__init__(position, size, sliderBG, knob)
        self.colorPicker = hsvColorPicker

    def onKnobChange(self):
        newH = self.getKnobValue() * 360
        newColor = HSVColorPicker.HSVToRGB((newH, 1, 1))
        w, h = self.getSize()
        knobSize = min(w, h)

        surface = Surface((knobSize, knobSize))
        surface.fill(newColor)
        draw.rect(surface, (0, 0, 0), (0, 0, knobSize, knobSize), HSVSlider.KNOB_THICKNESS)

        self.colorPicker.updateChroma(newH)

        self.updateKnob(surface)


    @staticmethod
    def __makeSliderBG(size):
        w, h = size

        surface = Surface((w, h))
        
        blockWidth = w / 360
        blockSize = (ceil(blockWidth), h)
        for h in range(360):
            colorBlock = Surface(blockSize)
            colorBlock.fill(HSVColorPicker.HSVToRGB((h, 1, 1)))
            surface.blit(colorBlock, (h * blockWidth, 0))
        
        return surface 

    @staticmethod
    def __makeKnob(size):
        w, h = size 
        knobSize = min(w, h)

        surface = Surface((knobSize, knobSize))
        surface.fill(HSVColorPicker.HSVToRGB((0, 1, 1)))
        draw.rect(surface, (0, 0, 0), (0, 0, knobSize, knobSize), HSVSlider.KNOB_THICKNESS)

        return surface
    


