import matplotlib.pyplot as plt

def draw_line_dda(x1, y1, x2, y2):
    # Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the number of steps
    steps = max(abs(dx), abs(dy))

    # Calculate the increment for each step
    x_increment = dx / steps
    y_increment = dy / steps

    # Generate and store points
    x = x1
    y = y1
    x_values = []
    y_values = []

    for _ in range(int(steps) + 1):
        x_values.append(round(x))
        y_values.append(round(y))
        x += x_increment
        y += y_increment

    # Plot the line using Matplotlib
    plt.plot(x_values, y_values, marker="o", color="blue")
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    plt.show()

# Example usage
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

draw_line_dda(x1, y1, x2, y2)
