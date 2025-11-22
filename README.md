# LoRa Chirp Simulator

A Python simulator for LoRa chirps using NumPy and Matplotlib.
It generates up-chirps and plots their real part to visualize the LoRa signal.

---

## Installation

Make sure you have Python installed. Then install the required libraries:

```bash
python -m pip install numpy scipy matplotlib
```

---

## Running the code

In the terminal, navigate to the folder and run:

```bash
python LoRa.py
```

---

## Output

The program will display a graph of the LoRa up-chirp real part.
It also saves the plot as an image `chirp.png` in the same folder.

![LoRa Chirp](chirp.png)

---

## Technical Notes

* **Fs**: Sampling frequency
* **BW**: Bandwidth
* **SF**: Spreading Factor
* **Ts**: Symbol duration
* Uses linear up-chirps generated with complex exponentials
