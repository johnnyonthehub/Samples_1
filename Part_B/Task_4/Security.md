# `Task 3: Security`

## A:  SSH Key Located in ~/.ssh/authorized_keys

`ssh-rsa` 

AAAAB3NzaC1yc2EAAAADAQABAAABAQCaQHn/N7zgkWqDroONBRb0w28yEWgud8JYlHygJs6g54jaSFC4RECwE7QYZhAPhJaU7nT9wpPdt+aNi6rN5s2rIWIFeR2rkYcMV2kRN4IuoYOZx9qy/1JqOcR78hktiISyX0/gtVtLepVarNBmYSPr+Mb2gCOfVoLCrXUhSXMzKS+eTW3qMgZiZmnKM7UWRMJ+Klc+vH2t95MYd5FNGJXsuVF8iSUWeJ7lYeNIjDIkHIOEUrl7q8Sh+JY9XT7jnPCKDL0QkTvzggx3IYflwcf1tUah+c8a6C54+jHx/Kmwkz6IddOWdYSREXXYb2f8kCx1ksdmC65xCkbmX1H3+FTN vockey

`Algorithm Used: RSA`

## B: Command used to change` the API server port number which needs to be opened under security group settings

`uvicorn main:app --port 64308 --host`
(Refer to screenshot Image A)
To achieve this, first, a simple main.py file was created in the command line.  This command changes the port of the API it is to be deployed into, in this case, 64308.  (*SEE IMAGE IN TASK 4 SCREENSHOTS FOLDER)

## C: Name of the file and the line needed to change in order to change the SSH Server Port Number

`File:  sshd_config
Path /etc/ssh/sshd_config`

The line:  Port 22 CHANGED TO Port 15643

sshd_config handles all the configuration settings for the ssh daemon (background program).  In addition to setting the default port, the an authorised user would come here to configure public key authentication, password authentication, and root login permissions.


## D: Hashing algorithm chosen earlier for the /hash_password route

I used a SHA-256 hashing algorithm to accomplish this.

#### `STRENGTHS:`

* The 256 bit key that is generated makes it EXTREMELY unlikely that you would generate two identical hash keys (known as a 'collision'). To put it another way, it is capable of producing 2 to the power of 256 hash values. This makes brute force attacks an exercise in futility.
* The SHA-256 is an accepted industry standard.  Financial institutions rely on this method to encrypt customer passwords and other ID.
* If the hashed information is changed, even to a minor degree this will generate a completely new hash block. 
* Due to the nature of the algorithm, hashes can be generated very quickly, regardless of size.  Encrypting the Bible would take as long as "The quick brown fox.", and they would generate hashes of equal size.

#### `WEAKNESSES:`

* Theortically, the SHA-256 is vulnerable to length extension attacks.  This is where by simply knowing the length of the hash and the encrypted string, an attacker is able to determine which part of the hash is "padding" and reverse-engineer the hash by continuing it.
* Rainbow tables, utilities which are basically enormous dictionaries of possible passwords, their hashes and associated algorithms are another threat.  For this reason as well as th one above, it's advisable to add salt (and pepper) to the hash as an added layer of security.  Owners of passwords should also create them with random characters added.





