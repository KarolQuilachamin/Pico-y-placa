# Pico-y-placa

This program is a Peak and Plate simulator and consists of 4 files.
"biblioteca" in this file there are 3 functions that allow us to validate the three input data. "day" that allows entering the date and obtaining the day to which it corresponds, "time" that allows us to know if the entered time is within the range allowed by the Peak and Plate, and "plate" that returns the last digit of the plate entered.
"Hacedor "this file creates a random database of the three entries, that is, it creates 3 .txt files with random dates, plates and times with their respective validations.
"Leedor" this file works with the two previous files, it uses the "biblioteca" file to obtain the day, the last plate number and if the time is inside or outside the Pico y Placa hours. Perform this process for all the data that was generated in the "Hacedor" file. The functions of this file must be called to continue the process of the final program.
"Comparador" in this file the data of "Leedor" are compared in order to know if according to the input data, it is or is not in Pico y Placa hours according to plate.
The final result is in the file "FINALDOC.txt" that will be generated thanks to the previous files.
