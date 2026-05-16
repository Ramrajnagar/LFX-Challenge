#!/usr/bin/env python3
"""
Tower of Hanoi Visualization Script
Demonstrates the practical application of Recursion and Iteration.
"""

import time
import os

# Configuration
TOTAL_DISKS = 3
ANIMATION_DELAY = 1.0  # Seconds between frames

# Global state tracking for the game boards
pegs = {
    'A': list(range(TOTAL_DISKS, 0, -1)),  # Source peg holds all initial disks
    'B': [],                              # Auxiliary peg
    'C': []                               # Destination peg
}


def clear_terminal():
    """Clears the standard output stream for fluid visual frames."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_pegs():
    """
    ===========================================================================
    DEMONSTRATION OF ITERATION
    ===========================================================================
    This rendering pipeline relies strictly on nested iterative loops to map
    the current state arrays into a clean command-line graphical dashboard.
    """
    clear_terminal()
    print("=== TOWER OF HANOI VISUALIZER ===")
    print(f"Disks: {TOTAL_DISKS} | Delay: {ANIMATION_DELAY}s\n")
    
    # Outer Loop (Iterative vertical height scanning from top to bottom)
    for level in range(TOTAL_DISKS - 1, -1, -1):
        row_buffer = ""
        
        # Inner Loop (Iterative horizontal peg grid mapping)
        for peg_id in ['A', 'B', 'C']:
            current_stack = pegs[peg_id]
            
            # Check if a disk occupies this specific spatial coordinate
            if level < len(current_stack):
                disk_size = current_stack[level]
                # Construct symmetric graphics representing the disk size
                disk_str = ("=" * (disk_size * 2 - 1)).center(TOTAL_DISKS * 2 + 1)
                row_buffer += f" [{disk_str}] "
            else:
                # Render the structural core axis of the empty peg segment
                axis_str = "|".center(TOTAL_DISKS * 2 + 1)
                row_buffer += f"  {axis_str}  "
                
        print(row_buffer)
        
    # Render base foundation and identifiers
    base_width = (TOTAL_DISKS * 2 + 7) * 3
    print("-" * base_width)
    
    label_spacing = " " * (TOTAL_DISKS + 2)
    print(f"{label_spacing}Peg A{label_spacing}    {label_spacing}Peg B{label_spacing}    {label_spacing}Peg C")
    print("\n")
    
    time.sleep(ANIMATION_DELAY)


def execute_disk_move(source_peg, destination_peg):
    """Mutates the data arrays by moving a single disk and triggers a redraw."""
    moving_disk = pegs[source_peg].pop()
    pegs[destination_peg].append(moving_disk)
    print_pegs()


def solve_hanoi(n, source, destination, auxiliary):
    """
    ===========================================================================
    DEMONSTRATION OF RECURSION
    ===========================================================================
    This mathematical solver breaks down the structural problem of moving 'n' 
    disks by splitting it into smaller sub-problems that resolve themselves.
    """
    # BASE CASE: The absolute smallest unit of work. Stops the recursion loop.
    if n == 1:
        execute_disk_move(source, destination)
        return

    # RECURSIVE STEP 1: Shift the upper stack sub-tree safely out of the way
    solve_hanoi(n - 1, source, auxiliary, destination)

    # Core Action: Move the structural foundation disk to the target peg
    execute_disk_move(source, destination)

    # RECURSIVE STEP 2: Shift the sub-tree stack back onto the foundation disk
    solve_hanoi(n - 1, auxiliary, destination, source)


if __name__ == "__main__":
    try:
        # Render initial frame configuration
        print_pegs()
        input("Configuration initialized. Press [ENTER] to start the recursive solution...")
        
        # Start solver pipeline
        solve_hanoi(TOTAL_DISKS, 'A', 'C', 'B')
        print("Success: Challenge solved flawlessly.")
    except KeyboardInterrupt:
        print("\nProcess terminated by user.")