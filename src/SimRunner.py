from Simulation import Simulation

runner = Simulation()
if runner.command._reset:
    runner = Simulation()
runner.mainloop()