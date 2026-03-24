# # bad
# parrot(dog_bell): print("dog_bell")
# parrot(pst): print("pst")
# parrot(suck_teeth): print("suck_teeth")
# parrot(mouth_smack): print("mouth_smack")
# parrot(thhk): print("thhk")

# good
parrot(rawr):
	print("rawr")

parrot(smooch):
	print("smooch")

parrot(trot):
	    # close zoom if open
    tracking.zoom_cancel()
    mouse_click(0)
    # close the mouse grid if open
    user.grid_close()
    # End any open drags
    # Touch automatically ends left drags so this is for right drags specifically
    user.mouse_drag_end()
	
parrot(mouth_wink):
	print("mouth_wink")
		
parrot(pop):
	    # close zoom if open
    tracking.zoom_cancel()
    mouse_click(1)
    # close the mouse grid if open
    user.grid_close()
