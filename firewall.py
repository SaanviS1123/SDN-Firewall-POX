from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected")

def _handle_PacketIn(event):
    packet = event.parsed
    ip = packet.find('ipv4')

    if ip:
        src = str(ip.srcip)
        dst = str(ip.dstip)

        # BLOCK h1 -> h2
        if src == "10.0.0.1" and dst == "10.0.0.2":
            log.info(f"BLOCKED: {src} -> {dst}")
            return

        log.info(f"ALLOWED: {src} -> {dst}")

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    msg.in_port = event.port
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
