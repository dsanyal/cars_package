from bmw import bmw
from hyundai import hyundai
from honda import honda
from segment import car_segment

mod_bmw = bmw()

# Which models from BMW are on sale currently in India?
mod_bmw.outModels()

mod_honda = honda()
mod_hyundai = hyundai()

# How much does Hyundai Xcent cost in INR?
mod_hyundai.prices('Xcent')

# Is Honda city a hatchback or a sedan?
mod_honda.hback_or_sedan_or_suv('City')


brio = car_segment('Brio')

# Which car segment doe Honda brio belong to?
brio.find_segment()
