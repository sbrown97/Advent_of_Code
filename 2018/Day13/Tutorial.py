from IPython.display import display, clear_output
import matplotlib.pyplot as plt


class Cart:
    def __init__(self,symbol,x,direction):
        """create a cart a position x moving in a given direction"""
        self.symbol = symbol # icon for displaying the cart
        self.x = x # x coordinate
        self.direction = direction # +1 if cart is facing right -1 if facing left

    def step(self):
        """Execute one step for this cart"""
        self.x += self.direction # move the cart in the direction it is facing

def update_ax(ax,carts):
    """ plot all carts positions, using their symbol, on a horizontal line"""
    ax.cla()
    
    ax.set_xlim(0, 20)
    ax.set_ylim(0,2)
    ax.axis('off')
    
    ax.plot(range(20),[1]*20,color='blue')
    
    for c in carts:
        ax.plot(c.x, 1,marker=c.symbol)
    
    return ax

def run_simulation(carts,steps):
    """ run the simulation for the specified number of time steps"""
    
    # set up display
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    ax = update_ax(ax,carts)
    display(fig)
    clear_output(wait = True)
    plt.pause(0.5)
        
    for t in range(steps): # for each time step
            
        for c in carts: # for each cart
            c.step() # execute a step for the cart
            fig = update_ax(ax,carts)
            display(fig)
            clear_output(wait=True)
            plt.pause(0.5)

""" 1 cart moving right """

cart1 = Cart('>',0,1)

run_simulation([cart1],20)
            
