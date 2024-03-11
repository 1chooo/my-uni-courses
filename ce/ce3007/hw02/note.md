# Computer Network HOMEWORK 2 Note

1. In our RDT protocols, why did we need to introduce checksums?
    - Solution To detect packet corruption during transmission.
2. In our RDT protocols, why did we need to introduce sequence numbers?
    - Solution Sequence numbers are required for a receiver to determine whether an arriving packet contains new data or is a retransmission, to support re-ordering, and provide some information about potentially dropped packets.
3. In our RDT protocols, why did we need to introduce acknowledgements?
    - Solution Acknowledgements of some form are necessary to provide feedback to the sending host, so the sending host can know whether packets were successfully received.
4. In our RDT protocols, why did we need to introduce timers?
    - Solution Timers were introduced to detect lost packets. If the ACK for a transmittedpacket is not received within the duration of the timer for the packet, the packet (or its ACK or NACK) is assumed to have been lost. Hence, the packet is retransmitted.