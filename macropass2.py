class MacroPass2:
    def __init__(self):
        # The Macro Name Table (MNT), Macro Definition Table (MDT), and Argument List Array (ALA)
        self.mnt = []
        self.mdt = []
        self.ala = []

    def define_macro(self, name, param_list, body):
        """
        Define a macro and add its details to the MNT and MDT.
        """
        # Store the macro details in the MNT
        self.mnt.append({
            'macro_name': name,
            'mdt_index': len(self.mdt) + 1,  # MDT index starts from 1
            'params': param_list
        })

        # Add the body lines of the macro to the MDT
        for line in body:
            self.mdt.append(line)

    def add_to_ala(self, actual_params):
        """
        Add actual parameters for a macro invocation to the ALA.
        """
        self.ala.append(actual_params)

    def substitute_parameters(self, line, actual_params, param_names):
        """
        Substitute the actual parameters into the macro body line.
        """
        for i, param in enumerate(param_names):
            if param in line:
                if i < len(actual_params):
                    line = line.replace(param, actual_params[i])
                else:
                    # If there's no actual parameter passed, replace with default (if any)
                    default_value = param.split('=')[1] if '=' in param else ''
                    line = line.replace(param, default_value)
        return line

    def macro_pass_2(self):
        """
        Perform Macro Pass 2: Substitute parameters into macro bodies.
        """
        output = []
        
        for idx, (actual_params, mnt_entry) in enumerate(zip(self.ala, self.mnt)):
            # Get the parameters for the macro from MNT
            param_names = mnt_entry['params'].split(', ')
            param_names = [param.split('=')[0] for param in param_names]  # Get formal parameter names only
            
            # Get the macro body from MDT starting from the index in MNT
            mdt_index = mnt_entry['mdt_index']
            macro_body = self.mdt[mdt_index - 1:mdt_index + len(param_names) - 1]  # Getting the lines of the macro body
            
            # Substitute parameters for each line of the macro body
            for line in macro_body:
                transformed_line = self.substitute_parameters(line, actual_params, param_names)
                output.append(transformed_line)
        
        # Return the output after substitution
        return output

    def print_result(self, output):
        """Print the output after macro pass 2."""
        print("\nAfter Macro Pass 2:")
        print("---------------------------------------------------------")
        for line in output:
            print(line)
        print("---------------------------------------------------------")

# Define the macros and the program for Macro Pass 2
macro_processor = MacroPass2()

# Define first macro INCR
incr_body = [
    "MOVER &REG, &X",     # MOVER &REG, &X
    "ADD &REG, &Y",       # ADD &REG, &Y
    "MOVEM &REG, &X",     # MOVEM &REG, &X
    "MEND"
]
macro_processor.define_macro("INCR", "&X, &Y, &REG=AREG", incr_body)

# Define second macro DECR
decr_body = [
    "MOVER &REG, &A",     # MOVER &REG, &A
    "SUB &REG, &B",       # SUB &REG, &B
    "MOVEM &REG, &A",     # MOVEM &REG, &A
    "MEND"
]
macro_processor.define_macro("DECR", "&A, &B, &REG=BREG", decr_body)

# Add actual parameters to the ALA for macro invocations
macro_processor.add_to_ala(["N1", "N2", "REG=CREG"])    # INCR N1, N2, REG=CREG
macro_processor.add_to_ala(["N1", "N2"])               # DECR N1, N2

# Perform Macro Pass 2
output = macro_processor.macro_pass_2()

# Print the result after Macro Pass 2
macro_processor.print_result(output)
