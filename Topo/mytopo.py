"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        attacker = self.addHost('lh', ip='10.1.1.1')
        user = self.addHost('rh', ip='10.1.1.2')
        switch = self.addSwitch('s1')

        # Add links
        self.addLink(attacker, switch)
        self.addLink(user, switch)

topos = {'mytopo': (lambda: MyTopo())}
