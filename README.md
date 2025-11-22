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

![LoRa Chirp]<img width="1916" height="965" alt="LoRa-Chirp" src="https://github.com/user-attachments/assets/a4dfd888-656a-4e9f-bd84-9fc2b2515445" />


---

## Technical Notes

* **Fs**: Sampling frequency
* **BW**: Bandwidth
* **SF**: Spreading Factor
* **Ts**: Symbol duration
* Uses linear up-chirps generated with complex exponentials
