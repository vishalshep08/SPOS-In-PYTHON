class Macro:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params  # List of parameters for the macro
        self.body = body      # List of body lines for the macro

class MacroPass1:
    def __init__(self):
        self.mnt = []  # Macro Name Table (MNT)
        self.mdt = []  # Macro Definition Table (MDT)
        self.ala = []  # Argument List Array (ALA)

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

    def print_mnt(self):
        """Print the Macro Name Table (MNT)."""
        print("Macro Name Table (MNT):")
        print("---------------------------------------------------------")
        print("Macro Name | MDT Index | Parameters")
        for entry in self.mnt:
            print(f"{entry['macro_name']:<11} | {entry['mdt_index']:<9} | {entry['params']}")
        print("---------------------------------------------------------")

    def print_mdt(self):
        """Print the Macro Definition Table (MDT)."""
        print("\nMacro Definition Table (MDT):")
        print("---------------------------------------------------------")
        print("Line Number | Instruction")
        for i, line in enumerate(self.mdt):
            print(f"{i + 1:<12} | {line}")
        print("---------------------------------------------------------")

    def print_ala(self):
        """Print the Argument List Array (ALA)."""
        print("\nArgument List Array (ALA):")
        print("---------------------------------------------------------")
        for i, args in enumerate(self.ala):
            print(f"Macro Call {i+1}: {args}")
        print("---------------------------------------------------------")

# Example usage of MacroPass1 class
macro_processor = MacroPass1()

# Define first macro M1
m1_body = [
    "MOVER &A, &X",     # MOVER &A, &X
    "ADD &A, ='1'",     # ADD &A, ='1'
    "MOVER &B, &Y",     # MOVER &B, &Y
    "ADD &B, ='5'",     # ADD &B, ='5'
    "MEND"
]
macro_processor.define_macro("M1", "&X, &Y, &A=AREG, &B=", m1_body)

# Define second macro M2
m2_body = [
    "MOVER &U, &P",     # MOVER &U, &P
    "MOVER &V, &Q",     # MOVER &V, &Q
    "ADD &U, ='15'",    # ADD &U, ='15'
    "ADD &V, ='10'",    # ADD &V, ='10'
    "MEND"
]
macro_processor.define_macro("M2", "&P, &Q, &U=CREG, &V=DREG", m2_body)

# Add actual parameters to the ALA for macro invocations
macro_processor.add_to_ala(["10", "20", "&B=CREG"])    # M1 10, 20, &B=CREG
macro_processor.add_to_ala(["100", "200", "&V=AREG", "&U=BREG"])  # M2 100, 200, &V=AREG, &U=BREG

# Print MNT, MDT, and ALA tables
macro_processor.print_mnt()
macro_processor.print_mdt()
macro_processor.print_ala()
