### Credentials stuffing and generation roles


Roles to (re)generate and/or populate credentials into AWS SSM Parameter Store.


The credentials can either be pre-existing or generated on the fly, if they exist by default they do not overwrite the contents of the
existing credential set.

#### Variables provided by the playbook
The playbook is required to provide `account` and `environment` as input variables

 - `account` - the descriptive account name, synonymous with product ie `vcms` or `engineering`
 - `environment_name` - this is the environment we're targeting, ie `dev` or `prod`

#### Data types
- ##### String Entry
    A simple predefined string that can be stored encrypted or in the clear

    The metadata and variables associated are below
    ```yaml
    - name: <Required> #The name of the entry
      ssm_type: <Optional> # Either String or SecureString defaults to String
      value: <Required> # The contents of our string
      overwrite: <Optional> #Do we want to replace the value on each run, default False
      type: string #required
    ```
- ##### Password Entry
    Either a predefined password or an entry to generate a password

    The metadata and variables associated are below
    ```yaml
    - name: <Required> #The name of the entry
      value: <Optional> # The contents of our password
      password_length: <Optional> #The number of characters our password is to be
      overwrite: <Optional> #Do we want to replace the value on each run, default False
      type: password #required
    ```

- ##### SSH-Key Entry
    Either a predefined key or an entry to generate a new one

    The metadata and variables associated are below
    ```yaml
    - name: <Required> #The name of the entry
      public_key: <Optional> # The contents of the public key, if private_key is set and this is empty, will be generated
      private_key: <Optional> # The contents of the private key
      hasPassword: <Optional> # If this is set, a password will be generated for key creation
      overwrite: <Optional> #Do we want to replace the value on each run, default False
      type: password #required
    ```

#### Example metadata
```yaml
products:
  # This is the namespace root key, we can have multiples
- name: root
  namespaces:
    # Service level key ie jenkins/gitlab/github
  - name: testing
    roles:
    - creds:
        # Stores an encrypted predefined string as a password
      - name: my_password
        value: password1
        type:  password
        #Generates a 64 character random password
      - name: my_secret_password
        type: password
        password_length: 64
        #Generates a random password will regenerate each play
      - name: my_secret_changing_password
        type: password
        password_length: 64
        overwrite: True
        # Stores a predefined string in the clear
      - name: my_clear_string
        value: "Hello World"
        type: string
        # Stores a predefined string in an encrypted format
      - name: my_secure_string
        value: "This is not the string you are looking for"
        type: string
        ssm_type: SecureString
        # Generates a ssh key with a random passphrase, the public key is stored in clear
      - name: my_secure_ssh_key
        type: ssh-key
        hasPassword: True
        # Regenerates a ssh key with a random passphrase, the public key is stored in clear
      - name: my_random_secure_ssh_key
        type: ssh-key
        hasPassword: True
        overwrite: True
        # Generates a ssh key with no passphrase, public key is stored in clear
      - name: my_ssh_key
        type: ssh-key
        # Loads a predefined ssh-pair, public key is stored in clear
      - name: my_existing_ssh_key
        type: ssh-key
        public_key: "public key string"
        private_key: "private key string"
        # Loads a predefined ssh-pair without a public key, public key is generated then stored in clear
      - name: my_existing_ssh_key_no_pub
        type: ssh-key
        private_key: "private key string"
```

Credentials generated from above are stored in a qualfied name `/<environment>/<account>/<namespace_root>/<service>/<credential_name>`

#### Assume Role

In order to have the credential stored in a specific secondary account any of the Data Types listed above can have the three following variables added.

````yaml
  - account_id: #AWS child account id
    role_name: #delegated role name
    is_delegated: #True for credential stored on separate account
````

#### Example metadata with sub account
```yaml
products:
  # This is the namespace root key, we can have multiples
- name: root
  namespaces:
    # Service level key ie jenkins/gitlab/github
  - name: testing
    roles:
    - creds:
        # Stores an encrypted predefined string as a password
      - name: my_password
        value: password1
        type:  password
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        #Generates a 64 character random password
      - name: my_secret_password
        type: password
        password_length: 64
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        #Generates a random password will regenerate each play
      - name: my_secret_changing_password
        type: password
        password_length: 64
        overwrite: True
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        # Stores a predefined string in the clear
      - name: my_clear_string
        value: "Hello World"
        type: string
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        # Stores a predefined string in an encrypted format
      - name: my_secure_string
        value: "This is not the string you are looking for"
        type: string
        ssm_type: SecureString
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        # Generates a ssh key with a random passphrase, the public key is stored in clear
      - name: my_secure_ssh_key
        type: ssh-key
        hasPassword: True
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        # Regenerates a ssh key with a random passphrase, the public key is stored in clear
      - name: my_random_secure_ssh_key
        type: ssh-key
        hasPassword: True
        overwrite: True
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        # Generates a ssh key with no passphrase, public key is stored in clear
      - name: my_ssh_key
        type: ssh-key
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        # Loads a predefined ssh-pair, public key is stored in clear
      - name: my_existing_ssh_key
        type: ssh-key
        public_key: "public key string"
        private_key: "private key string"
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
        # Loads a predefined ssh-pair without a public key, public key is generated then stored in clear
      - name: my_existing_ssh_key_no_pub
        type: ssh-key
        private_key: "private key string"
        account_id: 123456789987
        role_name: "admin"
        is_delegated: True
```
