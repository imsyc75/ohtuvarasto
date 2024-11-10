"""
Tests for the Varasto class.
"""

import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """Test cases for the Varasto class."""

    def setUp(self):
        """Set up a new Varasto instance before each test."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Test that the constructor creates an empty Varasto."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Test that the new Varasto has the correct capacity."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Test that adding to the Varasto increases the balance."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Test that adding to the Varasto decreases the available space."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Test that taking from the Varasto returns the correct amount."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Test that taking from the Varasto increases available space."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus(self):
        """Test that a Varasto with negative capacity is set to 0."""
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        """Test that a Varasto with a negative initial balance is set to 0."""
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alkusaldo_yli_tilavuuden(self):
        """Test that an initial balance greater than 
        capacity is set to capacity."""
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisaa_negatiivinen_maara(self):
        """Test that adding a negative amount does not change the balance."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_yli_tilavuuden(self):
        """Test that adding more than the capacity 
        sets the balance to capacity."""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen_maara(self):
        """Test that taking a negative amount returns 0 
        and does not change the balance."""
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_enemman_kuin_saldo(self):
        """Test that taking more than the balance 
        returns the current balance and sets it to 0."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijono_esitys(self):
        """Test the string representation of the Varasto."""
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
