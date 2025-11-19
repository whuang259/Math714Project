import numpy as np
import matplotlib.pyplot as plt

def set_3d_axes_equal(ax: plt.Axes) -> None:
    """
    Make axes of 3D plot have equal scale

    Parameters
    ----------
    ax : matplotlib axis
        The axis to set equal scale

    Reference
    ---------
    karlo, https://stackoverflow.com/questions/13685386/how-to-set-the-equal-aspect-ratio-for-all-axes-x-y-z
    """

    x_limits = ax.get_xlim3d()  # type: ignore
    y_limits = ax.get_ylim3d()  # type: ignore
    z_limits = ax.get_zlim3d()  # type: ignore

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])  # type: ignore
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])  # type: ignore
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])  # type: ignore


def plot_3d_trajectory(
    sol_x: np.ndarray,
    x_size, y_size,
    labels: list,
    colors: list,
    legend: bool,
) -> None:
    fig = plt.figure(figsize=(x_size, y_size))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_zlabel("$z$")  # type: ignore

    for i in range(sol_x.shape[1]):
        traj = ax.plot(
            sol_x[:, i, 0],
            sol_x[:, i, 1],
            sol_x[:, i, 2],
            color=colors[i],
        )
        # Plot the last position with marker
        ax.scatter(
            sol_x[-1, i, 0],
            sol_x[-1, i, 1],
            sol_x[-1, i, 2],
            marker="o",
            color=traj[0].get_color(),
            label=labels[i],
        )

    set_3d_axes_equal(ax)

    if legend:
        ax.legend(loc="center right", bbox_to_anchor=(1.325, 0.5))
        fig.subplots_adjust(right=0.7)

    plt.show()