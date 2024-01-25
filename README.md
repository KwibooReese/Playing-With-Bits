This is some code I wrote to play around with using bits for permissions.
In the code if you are a human, your permission = 0001 (4 permissions, 4 bits to represent them)
If you are a cat, your permission = 5, which is 0101
I used the bitwise operator & to compare them

Lets say you are a cat and want to use the woof function, what happens?
We know the permission for cat = 5
From the self.all_permissions dictionary we can see that the woof function is 2
So we do 5 & 2, which is:
0010 & 0101
none of the bits are the same so the result is 0000, so we don't allow the cat to woof
If 0 is returned, we know that animal does not have the permission to use that certain function
