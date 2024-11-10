"""
This module defines the Varasto class, 
which simulates a storage unit with methods to add and
remove items and track the available space.
"""

class Varasto:
    """Class representing a storage unit with methods 
    to add and remove items."""
    def __init__(self, tilavuus, alku_saldo=0):
        """Initialize the Varasto with a given capacity 
        and an initial balance."""
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # Invalid capacity, set to 0.0
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # Invalid initial balance, set to 0.0
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # Initial balance fits within capacity
            self.saldo = alku_saldo
        else:
            # Fill to capacity and discard the rest
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """Calculate and return the remaining capacity of the Varasto."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Add a given amount to the Varasto if it is valid."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Remove a given amount from the Varasto 
        and return the amount removed."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        """Return a string representation of the Varasto's current balance 
        and remaining capacity."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
