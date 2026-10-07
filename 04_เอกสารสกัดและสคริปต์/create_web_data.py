# -*- coding: utf-8 -*-
"""
Script to build data/questions90.js, data/flashcards.js, and data/summary.js
for COM2703 Computer Network Final Review Web Application
"""
import os
import json

base_dir = r"c:\Users\chinj\OneDrive\ปี3\COM2703-เครือข่าย"
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# ==========================================
# 1. QUESTIONS 90
# ==========================================
questions = [
    # Q1
    {
        "id": 1,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโตคอล IP ทำงานใน OSI Model Layer ใด",
        "options": ["Layer ที่ 6", "Layer ที่ 3", "Layer ที่ 5", "Layer ที่ 4"],
        "answer": 1,
        "explanation": "โพรโตคอล IP (Internet Protocol) ทำงานใน Layer 3 (Network Layer) ทำหน้าที่ระบุที่อยู่ (IP Address) และค้นหาเส้นทางส่งแพ็กเก็ตข้อมูล"
    },
    # Q2
    {
        "id": 2,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "Topology ใด ที่ปลายสายสัญญาณต้องมีเทอร์มิเนเตอร์ เพื่อดูดกลืนสัญญาณ",
        "options": ["MESH", "STAR", "BUS", "RING"],
        "answer": 2,
        "explanation": "โทโพโลยีแบบ BUS ใช้สายแกนร่วมเส้นเดียว ปลายสายทั้งสองด้านต้องมี Terminator เพื่อดูดกลืนสัญญาณ ป้องกันคลื่นสะท้อนกลับ (Echo) ที่จะรบกวนข้อมูล"
    },
    # Q3
    {
        "id": 3,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโตคอล FTP ทำงานใน OSI Model Layer ใด",
        "options": ["Layer ที่ 6", "Layer ที่ 7", "Layer ที่ 1", "Layer ที่ 2"],
        "answer": 1,
        "explanation": "FTP (File Transfer Protocol) เป็นบริการถ่ายโอนแฟ้มข้อมูลระหว่าง Client กับ Server จัดอยู่ใน Layer 7 (Application Layer)"
    },
    # Q4
    {
        "id": 4,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใด เป็นระบบเครือข่ายเฉพาะกลุ่มที่ให้บริการแก่สมาชิกในกลุ่มของตนเท่านั้น ผ่านเครือข่ายสาธารณะ",
        "options": ["Private Network", "Virtual Private Network", "Public Network", "Packet Distributed Network"],
        "answer": 1,
        "explanation": "Virtual Private Network (VPN) คือเครือข่ายเสมือนเฉพาะกลุ่มที่ส่งข้อมูลเข้ารหัสผ่านเครือข่ายสาธารณะ (Internet) เพื่อให้สมาชิกสื่อสารกันได้อย่างปลอดภัย"
    },
    # Q5
    {
        "id": 5,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ระบบเครือข่ายห้องปฏิบัติการคอมพิวเตอร์ ของภาควิชาคอมพิวเตอร์ มหาวิทยาลัยราชภัฏเชียงใหม่ เป็นแบบใด",
        "options": ["LAN", "VPN", "WAN", "MAN"],
        "answer": 0,
        "explanation": "ระบบเครือข่ายภายในห้องปฏิบัติการคอมพิวเตอร์ หรืออาคารเดียวกัน มีรัศมีการเชื่อมต่อไม่เกิน 10 กิโลเมตร จัดเป็นเครือข่ายท้องถิ่นหรือ LAN"
    },
    # Q6
    {
        "id": 6,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใดเหมาะที่จะนำมาใช้ในกรณีที่โหนดผู้รับและผู้ส่งมีการติดต่อกันอยู่เป็นประจำ และมีการแลกเปลี่ยนข้อมูลปริมาณมาก",
        "options": ["Digital Service", "Datagram Service", "Switch Virtual Circuit", "Permanent Virtual Circuit"],
        "answer": 3,
        "explanation": "Permanent Virtual Circuit (PVC) คือวงจรเสมือนถาวร มีการกำหนดเส้นทางไว้อย่างถาวรเหมือนสายเช่า (Leased Line) เหมาะสำหรับการสื่อสารเป็นประจำและมีข้อมูลปริมาณมาก"
    },
    # Q7
    {
        "id": 7,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "Topology ใด ที่มีการเชื่อมต่ออุปกรณ์ต่างๆ เข้ากันเป็นวงกลม",
        "options": ["RING", "STAR", "MESH", "BUS"],
        "answer": 0,
        "explanation": "โทโพโลยีแบบ RING (วงแหวน) โหนดจะเชื่อมต่อกันเป็นวงกลม โดยส่งข้อมูลไหลเวียนไปในทิศทางเดียวกัน"
    },
    # Q8
    {
        "id": 8,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ข้อใดเป็นมาตรฐานใดที่นำ Coaxial มาใช้",
        "options": ["10 Base F", "10 Base X", "10 Base 2", "10 Base T"],
        "answer": 2,
        "explanation": "10 Base 2 (Thin Coaxial) และ 10 Base 5 (Thick Coaxial) ใช้สายโคแอกเชียล ส่วน 10 Base T ใช้สาย UTP และ 10 Base F ใช้ Fiber Optic"
    },
    # Q9
    {
        "id": 9,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใดคือ วิธีการส่งแพ็กเกตที่แต่ละแพ็กเกตจะเป็นอิสระแก่กัน แพ็กเกตที่ส่งไปยังผู้รับเดียวกันอาจใช้เส้นทางต่างกัน และไปถึงผู้รับในลำดับที่แตกต่าง",
        "options": ["Digital Service", "Datagram Service", "Permanent Virtual Circuit", "Switch Virtual Circuit"],
        "answer": 1,
        "explanation": "Datagram Service เป็นบริการส่งแพ็กเกตแบบ Connectionless ที่แต่ละแพ็กเกตเดินทางอิสระ อาจใช้คนละเส้นทางและถึงปลายทางสลับลำดับกันได้"
    },
    # Q10
    {
        "id": 10,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "Internet Service Provider มีหน้าที่อะไร",
        "options": ["หน่วยงานกลางที่ดูแลการเชื่อมต่อเครือข่ายอินเทอร์เน็ต", "หน่วยงานที่บริหารคลื่นความถี่ในการสื่อสาร", "หน่วยงานวิจัยเกี่ยวกับอินเทอร์เน็ต", "หน่วยงานรักษาความปลอดภัยด้านอินเทอร์เน็ต"],
        "answer": 0,
        "explanation": "Internet Service Provider (ISP) คือผู้ให้บริการเชื่อมต่อเครือข่ายอินเทอร์เน็ต เช่น True, 3BB, AIS เพื่อให้ผู้ใช้สามารถเข้าถึงอินเทอร์เน็ตได้"
    },
    # Q11
    {
        "id": 11,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "สายสัญญาณในข้อใดต่อไปนี้ มีความเร็วสูงสุดใช้ได้ในระบบเครือข่าย Gigabit Ethernet เท่านั้น",
        "options": ["CAT6e", "CAT6", "CAT5e", "CAT5"],
        "answer": 0,
        "explanation": "CAT6 / CAT6e ออกแบบมาเพื่อรองรับความเร็วระดับ Gigabit และ 10-Gigabit Ethernet ในระยะทางที่กำหนด โดย CAT6e ให้ประสิทธิภาพแบนด์วิดท์สูงสุดในตัวเลือก"
    },
    # Q12
    {
        "id": 12,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "เทคนิคการส่งข้อมูลแบบใด ที่มีการแบ่งข้อมูลออกเป็นส่วนเล็ก ๆ ที่มีขนาดเท่ากันหมด และส่งข้อมูลด้วยเทคนิคพิเศษเรียกว่า Pipelining",
        "options": ["Packet-Switch", "Circuit-Switch", "Message-Switch", "Cell-Switch"],
        "answer": 0,
        "explanation": "Packet-Switching Network มีการแบ่งข้อมูลออกเป็นส่วนย่อยขนาดเท่ากันเรียกว่า Packet และสามารถส่งต่อเนื่องด้วยเทคนิค Pipelining"
    },
    # Q13
    {
        "id": 13,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "ข้อใด เป็นโพรโตคอลที่ควบคุมการรับส่งข้อมูลในเครือข่ายอินเทอร์เน็ต โดยมีการตรวจสอบยืนยันการส่ง-รับข้อมูลว่าส่งถึงปลายทางหรือไม่",
        "options": ["UDP", "SSL", "TCP", "PPTP"],
        "answer": 2,
        "explanation": "TCP (Transmission Control Protocol) ทำงานแบบ Connection-Oriented มีการตรวจสอบยืนยัน (Ack) การรับ-ส่งข้อมูลว่าถึงปลายทางอย่างถูกต้องและครบถ้วน"
    },
    # Q14
    {
        "id": 14,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "ข้อใดเป็นคุณสมบัติของโพรโตคอล DHCP",
        "options": ["ใช้ในการค้นหา IP Address ของเครื่องคอมพิวเตอร์ที่ต้องการติดต่อสื่อสารกัน", "ใช้ในการกำหนด MAC Address แบบอัตโนมัติให้กับเครื่องลูกข่าย", "ใช้ในการกำหนด IP Address แบบอัตโนมัติให้กับเครื่องลูกข่าย", "ถูกทุกข้อ"],
        "answer": 2,
        "explanation": "DHCP (Dynamic Host Configuration Protocol) ทำหน้าที่จัดสรรและกำหนดหมายเลข IP Address, Subnet Mask และ Gateway ให้เครื่องลูกข่ายแบบอัตโนมัติ"
    },
    # Q15
    {
        "id": 15,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใด คือระบบกระจายศูนย์ที่มีการวางโปรแกรมตามลักษณะการใช้งาน เช่น โปรแกรมกลุ่มบัญชีจะเก็บไว้ที่คอมพิวเตอร์แผนกบัญชีเท่านั้น โปรแกรมวิเคราะห์ข้อมูลและสร้างรายงานจะเก็บไว้ในส่วนของผู้บริหารระดับสูง",
        "options": ["ระบบกระจายศูนย์ตามวิธีการควบคุม (Distribution by Control)", "ระบบกระจายศูนย์ตามวิธีการประมวลผล (Distribution by Processing)", "ระบบกระจายศูนย์ตามหน้าที่การทำงาน (Distributed by Functions)", "ระบบกระจายศูนย์ตามตำแหน่งผู้ใช้ (Distribution by Location)"],
        "answer": 2,
        "explanation": "การจัดวางโปรแกรมและข้อมูลตามลักษณะงานหรือโครงสร้างแผนกขององค์กร จัดเป็นระบบกระจายศูนย์ตามหน้าที่การทำงาน (Distributed by Functions)"
    },
    # Q16
    {
        "id": 16,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใด เป็นวิธีการค้นหาเส้นทางที่ต้องเสียเวลาในการค้นหาเส้นทางเดินทุกครั้งที่จะส่งข้อมูล",
        "options": ["พลวัต (Dynamic)", "กระจายข่าย (Broadcast)", "สถิตย์ (Static)", "ตารางเส้นทาง (Route Table)"],
        "answer": 0,
        "explanation": "Dynamic / Adaptive Routing ปรับเปลี่ยนเส้นทางตลอดเวลาเพื่อเลี่ยงจุดเสีย แต่มีข้อเสียคือต้องเสียเวลาค้นหาเส้นทางที่ดีที่สุดใหม่ก่อนส่งข้อมูลทุกครั้ง"
    },
    # Q17
    {
        "id": 7,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "Topology ใด ที่มีการส่งผ่านข้อมูลแบบทิศทางเดียว",
        "options": ["RING", "BUS", "STAR", "MESH"],
        "answer": 0,
        "explanation": "Topology แบบ RING มีการส่งผ่านข้อมูลไหลวนไปในทิศทางเดียวจากโหนดหนึ่งไปยังอีกโหนดหนึ่งเป็นวงกลม"
    },
    # Q18
    {
        "id": 18,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโตคอลใด ที่ถูกใช้งานเมื่อมีการเรียกใช้คำสั่ง ping",
        "options": ["ICMP", "NETBIOS", "TCP/IP", "SSH"],
        "answer": 0,
        "explanation": "คำสั่ง ping ใช้โพรโทคอล ICMP (Internet Control Message Protocol) ในการส่ง Echo Request และรับ Echo Reply เพื่อตรวจสอบความพร้อมและการเชื่อมต่อของโฮสต์ปลายทาง"
    },
    # Q19
    {
        "id": 19,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "เทคนิคการส่งข้อมูลแบบใด ที่เป็นวงจรสื่อสารข้อมูลแบบสายเช่า (Leased Line) ที่จะถูกใช้งานโดยโหนดคู่ที่เป็นเจ้าของวงจรสื่อสารเท่านั้น ผู้อื่นจะไม่สามารถใช้เส้นทางเหล่านี้ได้",
        "options": ["Cell-Switch", "Packet-Switch", "Circuit-Switch", "Message-Switch"],
        "answer": 2,
        "explanation": "Circuit-Switching มีการจับจองวงจรสื่อสารตลอดเส้นทางระหว่างคู่สื่อสาร โดยผู้ใช้อื่นไม่สามารถเข้ามาใช้ช่องทางนี้ได้จนกว่าจะยุติการเชื่อมต่อ"
    },
    # Q20
    {
        "id": 20,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโตคอลข้อใด ที่มีการเข้ารหัสข้อมูลเพื่อความปลอดภัย",
        "options": ["ICMP", "HTTPS", "SIP", "FTP"],
        "answer": 1,
        "explanation": "HTTPS (Hypertext Transfer Protocol Secure) ใช้ SSL/TLS ในการเข้ารหัสข้อมูลที่รับส่งระหว่าง Browser กับ Web Server เพื่อป้องกันการดักฟัง"
    },
    # Q21
    {
        "id": 21,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใดคือ วิธีการส่งแพ็กเกตที่เหมาะสมกับการส่งข้อมูลสั้นๆ",
        "options": ["ถูกทุกข้อ", "Permanent Virtual Circuit", "Switch Virtual Circuit", "Datagram Service"],
        "answer": 3,
        "explanation": "Datagram Service เหมาะสำหรับการส่งข้อมูลที่มีขนาดสั้นๆ เพราะไม่มีขั้นตอนการสร้างวงจรล่วงหน้า ส่งแพ็กเกตออกไปได้ทันที"
    },
    # Q22
    {
        "id": 22,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ข้อใด คือ การเชื่อมต่อลิงค์เพื่อสื่อสารระหว่างสองอุปกรณ์โดยเฉพาะ",
        "options": ["Port-to-Port", "Multipoint", "Peer-to-Peer", "Point-to-Point"],
        "answer": 3,
        "explanation": "Point-to-Point คือการเชื่อมต่อสายสื่อสารระหว่างอุปกรณ์ 2 เครื่องโดยตรง ช่องทางการสื่อสารถูกจับจองเต็มที่ระหว่างทั้งสองตัว"
    },
    # Q23
    {
        "id": 23,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "Topology ใด ที่มี Hub เป็นศูนย์กลางควบคุมการสื่อสารทั้งหมด",
        "options": ["RING", "STAR", "MESH", "BUS"],
        "answer": 1,
        "explanation": "STAR Topology เชื่อมต่อทุกโหนดเข้าสู่ศูนย์กลางซึ่งคือ Hub หรือ Switch เป็นจุดรวมและกระจายสัญญาณ"
    },
    # Q24
    {
        "id": 24,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใด คือ ระบบเครือข่ายที่จำกัดการใช้งานเฉพาะกลุ่ม",
        "options": ["Internet", "Intranet", "WAN", "Client-Server"],
        "answer": 1,
        "explanation": "Intranet คือระบบเครือข่ายภายในองค์กร ที่จำกัดการเข้าถึงเฉพาะสมาชิกหรือพนักงานในองค์กรเท่านั้น บุคคลภายนอกไม่สามารถเข้าถึงได้"
    },
    # Q25
    {
        "id": 25,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "ข้อใด เป็นโพรโตคอลที่ใช้การเชื่อม VPN ต่อไปยังระบบเน็ตเวิร์กที่รองรับ",
        "options": ["UDP", "TCP", "SSL", "PPTP"],
        "answer": 3,
        "explanation": "PPTP (Point-to-Point Tunneling Protocol) อยู่ใน Layer 2 ถูกออกแบบมาเพื่อสร้างท่อเชื่อมต่อเครือข่ายเสมือน (VPN)"
    },
    # Q26
    {
        "id": 26,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "อุปกรณ์ใดที่ใช้เชื่อมต่อสายสัญญาณ ระหว่าง File Server กับ Workstation ในเครือข่ายแบบ Star",
        "options": ["Modem", "Server", "Switch", "Access Point"],
        "answer": 2,
        "explanation": "ในระบบเครือข่ายแบบ Star จะใช้อุปกรณ์ศูนย์กลางอย่าง Switch (หรือ Hub) เป็นตัวเชื่อมต่อสายสัญญาณระหว่างเครื่องลูกข่าย (Workstation) และเครื่องแม่ข่าย (File Server)"
    },
    # Q27
    {
        "id": 27,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโตคอล ที่ใช้งานอีเมล์แบบ Offline โดยทำการคัดลอกข้อมูลอีเมล์ทั้งหมดจากอีเมล์เซิร์ฟเวอร์ มายังเครื่องที่ทำการเชื่อมต่อ และลบข้อมูลในอีเมล์เซิร์ฟเวอร์",
        "options": ["IMAP", "POP3", "FTAM", "SMTP"],
        "answer": 1,
        "explanation": "POP3 (Post Office Protocol 3) ทำงานแบบ Offline ดาวน์โหลดอีเมลจากเซิร์ฟเวอร์มาเก็บไว้ในเครื่องลูกข่ายแล้วลบออกจากเซิร์ฟเวอร์"
    },
    # Q28
    {
        "id": 28,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "Topology ใด ต้องใช้สายสัญญาณจำนวนมากที่สุด เมื่อเปรียบเทียบกับแบบชนิดอื่น",
        "options": ["BUS", "RING", "STAR", "MESH"],
        "answer": 3,
        "explanation": "MESH Topology ต้องเชื่อมต่อทุกเครื่องเข้าหากันแบบจุดต่อจุดสมบูรณ์ จึงใช้สายสัญญาณมากที่สุด และมีค่าใช้จ่ายสูงสุด"
    },
    # Q29
    {
        "id": 29,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ระบบเครือข่าย แบบใดใช้สาย UTP ในการส่งผ่านข้อมูลด้วยความเร็วสูง (ระดับ Gigabit)",
        "options": ["WLAN", "Standard Ethernet", "1000 Base F", "1000 Base T"],
        "answer": 3,
        "explanation": "1000 Base T เป็นมาตรฐาน Gigabit Ethernet ที่ใช้สายคู่บิดเกลียวทองแดงแบบ UTP (Cat 5e หรือ Cat 6) ส่วน F คือ Fiber Optic"
    },
    # Q30
    {
        "id": 30,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใด เป็นเครือข่ายส่วนบุคคล",
        "options": ["VPN", "PAN", "Internet", "Intranet"],
        "answer": 1,
        "explanation": "PAN (Personal Area Network) คือเครือข่ายส่วนบุคคล มีระยะการเชื่อมต่อสั้นไม่เกิน 10 เมตร เช่น Hotspot, Bluetooth"
    },
    # Q31
    {
        "id": 31,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใด คือ ระบบเครือข่ายไร้สาย",
        "options": ["WAN", "WLAN", "VPN", "LAN"],
        "answer": 1,
        "explanation": "WLAN (Wireless Local Area Network) คือเครือข่ายท้องถิ่นแบบไร้สาย เช่น ระบบ Wi-Fi"
    },
    # Q32
    {
        "id": 32,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "ข้อใด เป็นโพรโตคอลที่ใช้เข้ารหัสข้อมูลที่ส่งในอินเทอร์เน็ต เช่น เว็บเพจ อีเมล์ เพื่อความปลอดภัย",
        "options": ["PPTP", "UDP", "SSL", "TCP"],
        "answer": 2,
        "explanation": "SSL (Secure Sockets Layer) ทำงานใน Layer 6 ทำหน้าที่เข้ารหัสข้อมูล (Encryption) ของเว็บเพจหรืออีเมลเพื่อความปลอดภัย"
    },
    # Q33
    {
        "id": 33,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโตคอลข้อใด ที่ทำหน้าที่ในการจับคู่ระหว่างแอดเดรสทางลอจิคัลกับแอดเดรสทางฟิสิคัล (MAC Address) เพื่อค้นหาว่าเครื่องที่มี IP address เป้าหมาย มีหมายเลข MAC address คืออะไร",
        "options": ["RARP", "TCP/IP", "ARP", "IPX/SPX"],
        "answer": 2,
        "explanation": "ARP (Address Resolution Protocol) ทำหน้าที่แปลงหมายเลขลอจิคัล (IP Address) ไปเป็นหมายเลขฟิสิคัล (MAC Address)"
    },
    # Q34
    {
        "id": 34,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "Topology ใด ใช้สายสัญญาณน้อยที่สุด เมื่อเปรียบเทียบกับการเชื่อมต่อแบบอื่น",
        "options": ["BUS", "STAR", "RING", "MESH"],
        "answer": 0,
        "explanation": "BUS Topology ใช้สายแกนร่วมเพียงเส้นเดียวเชื่อมต่อทุกเครื่องตลอดแนว จึงประหยัดและใช้สายสัญญาณน้อยที่สุด"
    },
    # Q35
    {
        "id": 35,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "HTTP เป็นโพรโทคอลที่ใช้ในการนำเสนอข้อมูลในบริการชนิดใด",
        "options": ["การอัพโหลดข้อมูล", "การรับ-ส่งอีเมล์", "เวิลด์ไวด์เว็บ", "การดาวน์โหลดข้อมูล"],
        "answer": 2,
        "explanation": "HTTP (Hypertext Transfer Protocol) ใช้สำหรับเรียกดูเอกสารและสื่อสารข้อมูลบนเวิลด์ไวด์เว็บ (WWW) ผ่านพอร์ต 80"
    },
    # Q36
    {
        "id": 36,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ข้อใดเป็นมาตรฐานใดที่นำ Fiber Optic มาใช้",
        "options": ["10 Base 2", "10 Base T", "10 Base 5", "10 Base F"],
        "answer": 3,
        "explanation": "10 Base F (F = Fiber) เป็นมาตรฐานที่ใช้สายใยแก้วนำแสง (Fiber Optic)"
    },
    # Q37
    {
        "id": 37,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "การเชื่อมต่อระบบเครือข่ายในห้องปฏิบัติการคอมพิวเตอร์ Topology แบบใดจึงจะเหมาะสมในการทำงานมากที่สุด",
        "options": ["STAR", "BUS", "MESH", "RING"],
        "answer": 0,
        "explanation": "STAR Topology นิยมใช้ในห้องปฏิบัติการมากที่สุด เพราะติดตั้งและดูแลง่าย หากสายของเครื่องใดเครื่องหนึ่งชำรุด เครื่องอื่นยังทำงานต่อได้ตามปกติ"
    },
    # Q38
    {
        "id": 38,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโตคอล HTTPS ทำงานใน OSI Model Layer ใด",
        "options": ["Layer ที่ 3", "Layer ที่ 6", "Layer ที่ 7", "Layer ที่ 4"],
        "answer": 2,
        "explanation": "HTTPS จัดเป็นโพรโทคอลในระดับ Layer 7 (Application Layer) สำหรับการเข้าถึงและแสดงผลเว็บเพจแบบเข้ารหัสความปลอดภัย"
    },
    # Q39
    {
        "id": 39,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "Topology ใด ที่เครื่องคอมพิวเตอร์ทุกเครื่องในเครือข่ายจะเชื่อมต่อแบบ point-to-point",
        "options": ["RING", "BUS", "STAR", "MESH"],
        "answer": 3,
        "explanation": "MESH Topology เป็นการเชื่อมต่อทุกโหนดเข้าหากันแบบ Point-to-Point โดยสมบูรณ์ เครื่องทุกคู่จะมีสายตรงเชื่อมถึงกัน"
    },
    # Q40
    {
        "id": 40,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ระบบในข้อใด ที่เครื่องคอมพิวเตอร์และอุปกรณ์ทุกชนิดที่เชื่อมต่อมีความเท่าเทียมกัน ไม่มีเครื่องใดเครื่องหนึ่งทำหน้าที่เป็นเซิร์ฟเวอร์โดยเฉพาะ",
        "options": ["Centralized Systems", "Distributed Systems", "Peer-to-peer", "Client/Server"],
        "answer": 2,
        "explanation": "ระบบ Peer-to-Peer ทุกเครื่องในเครือข่ายมีสิทธิและหน้าที่เท่าเทียมกัน (Peer Computers) ทั้งการประมวลผลและการใช้ทรัพยากร"
    },
    # Q41
    {
        "id": 41,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโทคอล RARP (Reverse ARP) ทำหน้าที่ใด และมักถูกนำไปใช้งานในกรณีใด",
        "options": [
            "แปลง IP Address เป็น MAC Address สำหรับส่งข้อมูล",
            "แปลง MAC Address เป็น IP Address สำหรับคอมพิวเตอร์ที่ไม่มีฮาร์ดดิสก์ (Diskless Computer)",
            "ตรวจสอบเส้นทางของแพ็กเก็ตข้อมูลบนอินเทอร์เน็ต",
            "เข้ารหัสข้อมูลในระดับ Session Layer"
        ],
        "answer": 1,
        "explanation": "RARP ทำหน้าที่ย้อนกลับกับ ARP คือแปลง MAC Address เป็น IP Address นิยมใช้กับคอมพิวเตอร์ที่ไม่มีดิสก์ (Diskless Computer) เพื่อสอบถาม IP จากเซิร์ฟเวอร์ขณะบูตเครื่อง"
    },
    # Q42
    {
        "id": 42,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "ข้อใดกล่าวถึงความแตกต่างระหว่าง TCP และ UDP ได้อย่างถูกต้อง",
        "options": [
            "TCP เป็น Connectionless ส่วน UDP เป็น Connection-Oriented",
            "TCP ไม่มีการตรวจสอบยืนยันข้อมูล ส่วน UDP ตรวจสอบยืนยันเสมอ",
            "TCP มีความน่าเชื่อถือสูงและตรวจสอบยืนยัน ส่วน UDP ส่งรวดเร็วแต่ไม่ตรวจสอบยืนยัน (Connectionless)",
            "TCP ใช้ส่งข้อมูล Real-time Streaming ส่วน UDP ใช้ส่งไฟล์ขนาดใหญ่ที่ห้ามสูญหาย"
        ],
        "answer": 2,
        "explanation": "TCP ตรวจสอบยืนยันการรับส่งและจัดลำดับข้อมูล (Connection-Oriented) จึงน่าเชื่อถือสูง ส่วน UDP ส่งข้อมูลแบบ Connectionless ไม่รอการยืนยัน ทำให้รวดเร็วกว่า เหมาะกับ VoIP และ Video Streaming"
    },
    # Q43
    {
        "id": 43,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโทคอลใดที่ใช้สำหรับการรับอีเมลแบบ Online โดยผู้ใช้สามารถเปิดอ่าน จัดโฟลเดอร์ และข้อมูลจะซิงก์ตรงกันทุกอุปกรณ์บนเซิร์ฟเวอร์",
        "options": ["POP3", "SMTP", "IMAP", "SNMP"],
        "answer": 2,
        "explanation": "IMAP (Internet Message Access Protocol) ทำงานแบบ Online จัดเก็บอีเมลไว้บน Mail Server ทำให้ข้อมูลซิงก์ตรงกันทุกอุปกรณ์ที่เข้าใช้งาน"
    },
    # Q44
    {
        "id": 44,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโทคอล SMTP (Simple Mail Transfer Protocol) มีหน้าที่หลักตามข้อใด",
        "options": [
            "ส่งอีเมลจากเครื่องผู้ส่งไปยังเซิร์ฟเวอร์ปลายทาง",
            "ดึงอีเมลจากเซิร์ฟเวอร์มาเก็บลงในคอมพิวเตอร์ลูกข่ายแบบ Offline",
            "แปลงชื่อโดเมนของเซิร์ฟเวอร์อีเมลเป็นหมายเลข IP",
            "เข้ารหัสรหัสผ่านของบัญชีอีเมล"
        ],
        "answer": 0,
        "explanation": "SMTP ใช้สำหรับ 'ส่งอีเมล' (Send mail) จากเครื่องไคลเอนต์ไปยัง Mail Server หรือส่งต่อระหว่าง Mail Server ด้วยกัน"
    },
    # Q45
    {
        "id": 45,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโทคอล MQTT (Message Queue Telemetry Transport) ได้รับการออกแบบมาเพื่อการสื่อสารในรูปแบบใดเป็นหลัก",
        "options": [
            "การถ่ายโอนไฟล์ภาพยนตร์ความละเอียดสูงในระบบ Cloud",
            "การสื่อสารระหว่างเครื่องต่อเครื่อง (M2M) และระบบ Internet of Things (IoT) ที่ต้องการประหยัดแบนด์วิดท์",
            "การส่งสัญญาณสตรีมมิ่งสดผ่านโครงข่ายโทรทัศน์",
            "การจัดการฐานข้อมูลขนาดใหญ่ระดับองค์กร"
        ],
        "answer": 1,
        "explanation": "MQTT เป็นโพรโทคอลน้ำหนักเบา (Lightweight) เหมาะสำหรับ Machine-to-Machine (M2M) และอุปกรณ์ IoT ที่มีข้อจำกัดด้านพลังงานและแบนด์วิดท์"
    },
    # Q46
    {
        "id": 46,
        "chapter": "บทที่ 5: โพรโทคอล & OSI Model",
        "question": "โพรโทคอล NetBIOS ทำงานใน OSI Model Layer ใด และมีหน้าที่หลักคืออะไร",
        "options": [
            "Layer 2 ทำหน้าที่ส่งต่อเฟรมข้อมูล",
            "Layer 4 ทำหน้าที่ตรวจสอบแพ็กเก็ตที่สูญหาย",
            "Layer 5 ทำหน้าที่เป็นตัวเชื่อม (Interface) ระหว่างระบบปฏิบัติการกับฮาร์ดแวร์เพื่อให้อัปพลิเคชันสื่อสารกับเครือข่ายได้",
            "Layer 7 ทำหน้าที่แสดงผลหน้าเว็บ"
        ],
        "answer": 2,
        "explanation": "NetBIOS ทำงานใน Layer 5 (Session Layer) เป็น Interface ตัวกลางระหว่าง OS กับเครือข่าย เพื่อให้ Application สามารถติดต่อสื่อสารผ่าน LAN ได้"
    },
    # Q47
    {
        "id": 47,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ในระบบ Packet-Switching การส่งแบบ Switched Virtual Circuit (SVC) แตกต่างจาก PVC อย่างไร",
        "options": [
            "SVC สร้างเส้นทางเสมือนแบบชั่วคราวเมื่อต้องการส่งข้อมูล ส่วน PVC เป็นเส้นทางเสมือนแบบถาวร",
            "SVC เหมาะกับการส่งข้อมูลสั้นๆ ส่วน PVC เหมาะกับเสียงสนทนา",
            "SVC มีค่าใช้จ่ายสูงกว่าสายเช่า Leased Line เสมอ",
            "SVC ไม่มีการใส่หมายเลขวงจรเสมือนในแพ็กเก็ต"
        ],
        "answer": 0,
        "explanation": "SVC (Switched Virtual Circuit) สร้างเส้นทางเสมือนขึ้นชั่วคราวขณะต้องการส่งข้อมูลปริมาณมากและคืนเส้นทางเมื่อเสร็จสิ้น ส่วน PVC (Permanent Virtual Circuit) กำหนดเส้นทางไว้อย่างถาวรเหมือนสายเช่า"
    },
    # Q48
    {
        "id": 48,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อด้อยที่สำคัญที่สุดของวิธีการค้นหาเส้นทางแบบสถิตย์ (Static Routing) คือข้อใด",
        "options": [
            "ต้องเสียเวลาคำนวณเส้นทางใหม่ก่อนส่งข้อมูลทุกครั้ง",
            "หากเส้นทางที่กำหนดไว้เกิดการชำรุดหรือสายขาด จะไม่สามารถส่งข้อมูลไปยังปลายทางได้",
            "เกิดการส่งข้อมูลซ้ำซ้อนกันหลายชุดในระบบ",
            "ใช้พลังงานการประมวลผลของ Router สูงมาก"
        ],
        "answer": 1,
        "explanation": "Static Routing กำหนดเส้นทางไว้ตายตัว หากเส้นทางชำรุด ระบบจะไม่สามารถเปลี่ยนไปใช้เส้นทางสำรองโดยอัตโนมัติ ทำให้ข้อมูลส่งไม่ถึงปลายทาง"
    },
    # Q49
    {
        "id": 49,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "วิธีการค้นหาเส้นทางแบบกระจายข่าวหรือฟลัดดิง (Flooding / Broadcast Routing) มีข้อเสียหลักคือข้อใด",
        "options": [
            "ข้อมูลจะไปไม่ถึงปลายทางแน่นอน",
            "ทำให้เกิดข้อมูลซ้ำซ้อน (Duplicate Packets) และสิ้นเปลืองแบนด์วิดท์ของระบบเครือข่าย",
            "ต้องใช้คอมพิวเตอร์ศูนย์กลางคำนวณเท่านั้น",
            "โหนดปลายทางจะไม่ได้รับข้อมูลที่ส่งไป"
        ],
        "answer": 1,
        "explanation": "Flooding ส่งสำเนาของแพ็กเก็ตออกไปทุกพอร์ต/ทุกโหนด ทำให้เกิดข้อมูลซ้ำซ้อนปริมาณมหาศาลและอาจทำให้เครือข่ายเกิดความคับคั่ง (Congestion)"
    },
    # Q50
    {
        "id": 50,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ระบบกระจายศูนย์ตามวิธีการประมวลผลแบบตามลำดับชั้น (Hierarchical Processing) มีลักษณะเด่นตามข้อใด",
        "options": [
            "ทุกเครื่องมีหน้าที่และอำนาจประมวลผลเท่าเทียมกันทั้งหมด",
            "รวมศูนย์ข้อมูลทั้งหมดไว้ที่เซิร์ฟเวอร์กลาง และแบ่งส่วนงานบางส่วนไปประมวลผลที่เครื่องลูกข่าย เช่น จุดชำระเงิน POS",
            "กระจายข้อมูลตามพื้นที่ทางภูมิศาสตร์ของเมือง",
            "ไม่มีการเชื่อมต่อสายสื่อสารระหว่างกัน"
        ],
        "answer": 1,
        "explanation": "แบบตามลำดับชั้น (Hierarchical) จะรวมข้อมูลหลักไว้ที่เซิร์ฟเวอร์ศูนย์กลาง ส่วนงานที่เหลือจะนำไปประมวลผลที่เครื่องลูกข่ายเฉพาะจุด เช่น เครื่องคิดเงิน POS"
    },
    # Q51
    {
        "id": 51,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "การเชื่อมต่อระบบเครือข่ายระยะไกลที่ครอบคลุมข้ามจังหวัด ประเทศ หรือทั่วโลก มักใช้สายสื่อสารแบบใด",
        "options": ["สายเคเบิลวงจรเช่า (Leased Line) ในระบบ WAN", "สายโทรศัพท์พื้นฐานแบบ Dial-up", "สาย Coaxial แบบ 10Base2", "คลื่นอินฟราเรดระยะสั้น"],
        "answer": 0,
        "explanation": "ระบบเครือข่ายวงกว้าง (WAN) ที่เชื่อมต่อระหว่างสาขาข้ามจังหวัดหรือประเทศ นิยมใช้สายสื่อสารวงจรเช่า (Leased Line) จากผู้ให้บริการโทรคมนาคม"
    },
    # Q52
    {
        "id": 52,
        "chapter": "บทที่ 6: ระบบเครือข่าย & Routing",
        "question": "ข้อใดอธิบายความแตกต่างระหว่าง Internet และ Intranet ได้ถูกต้องที่สุด",
        "options": [
            "Internet คือเครือข่ายเฉพาะภายในองค์กร ส่วน Intranet คือเครือข่ายสาธารณะทั่วโลก",
            "Internet คือเครือข่าย WAN สาธารณะทั่วโลก ส่วน Intranet เป็นเครือข่ายเฉพาะที่เข้าถึงได้เฉพาะบุคคลภายในองค์กร",
            "Internet ต้องใช้สายไฟเบอร์ออปติกเสมอ ส่วน Intranet ใช้ระบบไร้สายเท่านั้น",
            "ทั้งสองระบบไม่มีความแตกต่างกันในเชิงความปลอดภัย"
        ],
        "answer": 1,
        "explanation": "Internet คือเครือข่ายสาธารณะระดับโลกที่ทุกคนเข้าถึงได้ ส่วน Intranet คือเครือข่ายส่วนตัวขององค์กร ข้อมูลสงวนไว้เฉพาะพนักงานภายใน"
    },
    # Q53
    {
        "id": 53,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "หากอุปกรณ์ศูนย์กลาง เช่น Hub หรือ Switch ชำรุดเสียหาย จะส่งผลต่อเครือข่าย Topology แบบ Star อย่างไร",
        "options": [
            "ระบบจะตัดเฉพาะโหนดแรกออก และเครื่องที่เหลือยังทำงานได้ปกติ",
            "ระบบเครือข่ายทั้งหมดจะไม่สามารถทำงานและสื่อสารกันได้",
            "ระบบจะเปลี่ยนไปส่งข้อมูลแบบวงแหวนอัตโนมัติ",
            "ไม่มีผลกระทบใดๆ ต่อการสื่อสาร"
        ],
        "answer": 1,
        "explanation": "ใน Star Topology ศูนย์กลางคือ Single Point of Failure หาก Hub หรือ Switch เสียหาย ระบบเครือข่ายทั้งหมดจะไม่สามารถทำงานได้เลย"
    },
    # Q54
    {
        "id": 54,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "เครือข่ายแบบวงแหวน FDDI (Fiber Distributed Data Interface) มีลักษณะเด่นที่สำคัญตามข้อใด",
        "options": [
            "ใช้สายไฟเบอร์ออปติก 2 วงซ้อนกัน ข้อมูลวิ่งสวนทางกัน นิยมใช้เป็นเครือข่ายแกนหลัก (Backbone)",
            "ใช้สายทองแดงคู่บิดเกลียวแบบไม่หุ้มฉนวนวิ่งทิศทางเดียว",
            "มี Hub ศูนย์กลางคอยกระจายข้อมูล",
            "ไม่สามารถป้องกันสายขาดได้"
        ],
        "answer": 0,
        "explanation": "FDDI ใช้วงแหวนคู่สายใยแก้วนำแสง (Dual Ring) ส่งข้อมูลสวนทางกัน หากวงหนึ่งขาด อีกวงหนึ่งยังส่งข้อมูลต่อได้ นิยมใช้เป็น Backbone ความเร็วสูง"
    },
    # Q55
    {
        "id": 55,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "โทโพโลยีแบบ STAR-wire RING มีการนำอุปกรณ์ศูนย์กลางชนิดใดมาใช้เชื่อมต่อ เพื่อแก้ปัญหาโหนดเสียหาย",
        "options": ["MAU (Multistation Access Unit)", "Modem", "Repeater", "Gateway"],
        "answer": 0,
        "explanation": "STAR-wire RING ต่อสายแบบ Star เข้าสู่กล่องศูนย์กลางที่เรียกว่า MAU (Multistation Access Unit) ซึ่งมีวงแหวนอยู่ภายใน และสามารถตัดโหนดที่เสียออก (Bypass) ได้ทันที"
    },
    # Q56
    {
        "id": 56,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ประโยชน์หลักของ Proxy Server ในระบบเครือข่ายองค์กรคือข้อใด",
        "options": [
            "เก็บสำรองระบบปฏิบัติการของเครื่องลูกข่ายทั้งหมด",
            "เก็บข้อมูลหน้าเว็บที่เคยเปิด (Web Caching) ช่วยลดปริมาณ Data-stream และประหยัดแบนด์วิดท์",
            "แปลงหมายเลข MAC Address เป็น IP Address",
            "จ่ายกระแสไฟฟ้าผ่านสายแลนไปยังอุปกรณ์ปลายทาง"
        ],
        "answer": 1,
        "explanation": "Proxy Server ทำหน้าที่แคช (Cache) หน้าเว็บที่ผู้ใช้เคยเปิดไว้ เมื่อมีคำขอซ้ำจะดึงจาก Proxy แทนเว็บจริง ช่วยลด Data-stream และเพิ่มความเร็วในการท่องเว็บ"
    },
    # Q57
    {
        "id": 57,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ข้อใดอธิบายความแตกต่างระหว่าง Disk Server และ File Server ได้ถูกต้อง",
        "options": [
            "Disk Server ควบคุมพื้นที่และจัดสรรโควตาฮาร์ดดิสก์ให้ผู้ใช้ ส่วน File Server จัดการการจัดเก็บแฟ้มข้อมูล",
            "Disk Server เก็บฐานข้อมูล ส่วน File Server ควบคุมการพิมพ์",
            "Disk Server ให้บริการอีเมล ส่วน File Server ให้บริการเว็บ",
            "ทั้งสองตัวมีหน้าที่เหมือนกันทุกประการ"
        ],
        "answer": 0,
        "explanation": "Disk Server ควบคุมการแบ่งพื้นที่และโควตาของฮาร์ดดิสก์แก่ผู้ใช้ ส่วน File Server จัดเก็บและบริการแชร์ไฟล์แฟ้มข้อมูล"
    },
    # Q58
    {
        "id": 58,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "มาตรฐานเครือข่ายอีเทอร์เน็ต 100BASE-TX ตัวเลข 100 และตัวอักษร TX มีความหมายว่าอย่างไร",
        "options": [
            "ความเร็ว 100 Mbps และใช้สายคู่บิดเกลียว (Twisted pair)",
            "ระยะทาง 100 กิโลเมตร และใช้สายโคแอกเชียล",
            "รองรับ 100 อุปกรณ์ และส่งผ่านคลื่นวิทยุ",
            "ความเร็ว 100 Gbps และใช้สายใยแก้วนำแสง"
        ],
        "answer": 0,
        "explanation": "100 คือความเร็วในการส่งข้อมูล 100 Mbps (Fast Ethernet), BASE คือ Baseband และ TX คือการใช้สายทองแดงคู่บิดเกลียว (Twisted-Pair)"
    },
    # Q59
    {
        "id": 59,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "อุปกรณ์เครือข่ายชนิดใด ทำงานใน Data Link Layer (Layer 2) และใช้ตาราง MAC Address ในการส่งต่อข้อมูลเฉพาะพอร์ตปลายทาง",
        "options": ["Hub", "Repeater", "Switch", "Router"],
        "answer": 2,
        "explanation": "Switch (และ Bridge) ทำงานใน Layer 2 ตรวจสอบปลายทางด้วย MAC Address Table และส่งข้อมูลไปยังเฉพาะพอร์ตปลายทาง ไม่ส่งกระจายไปทุกพอร์ตเหมือน Hub"
    },
    # Q60
    {
        "id": 60,
        "chapter": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "question": "ข้อใดคือข้อดีและข้อเสียของการเชื่อมต่อแบบหลายจุด (Multidrop / Multipoint)",
        "options": [
            "ข้อดี: ส่งได้เร็วเต็มที่, ข้อเสีย: เปลืองสายสัญญาณมากที่สุด",
            "ข้อดี: ประหยัดสายสัญญาณ, ข้อเสีย: ข้อมูลอาจเกิดการชนกัน (Collision) ได้หากส่งพร้อมกัน",
            "ข้อดี: ปลอดภัยสูงสุด, ข้อเสีย: ไม่สามารถใช้กับคอมพิวเตอร์เกิน 2 เครื่องได้",
            "ข้อดี: ติดตั้งยาก, ข้อเสีย: มีค่าใช้จ่ายสูงกว่า Mesh"
        ],
        "answer": 1,
        "explanation": "Multidrop ใช้อุปกรณ์หลายตัวแชร์สายลิงก์เส้นเดียวกัน จึงประหยัดสายสื่อสาร แต่ข้อเสียคือมีโอกาสที่ข้อมูลจะชนกันได้หากส่งพร้อมกัน"
    },
    # Q61
    {
        "id": 61,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address แบบ IPv4 และ IPv6 ประกอบด้วยจำนวนบิตกี่บิตตามลำดับ",
        "options": ["16 บิต และ 64 บิต", "32 บิต และ 128 บิต", "32 บิต และ 64 บิต", "64 บิต และ 128 บิต"],
        "answer": 1,
        "explanation": "IPv4 ประกอบด้วยเลขฐานสอง 32 บิต (4 Octets) รองรับได้ 2^32 หมายเลข ส่วน IPv6 ประกอบด้วย 128 บิต (8 Hextets) รองรับได้ 2^128 หมายเลข"
    },
    # Q62
    {
        "id": 62,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IPv6 `3FFE:085B:1F1F:0000:0000:0000:00A9:1234` เมื่อเขียนในรูปแบบย่อที่ถูกต้องที่สุดจะเป็นข้อใด",
        "options": [
            "3FFE:85B:1F1F::A9:1234",
            "3FFE:85B:1F1F:0:0:0:A9:1234",
            "3FFE:085B:1F1F:::A9:1234",
            "3FFE:85B:1F1F::::A9:1234"
        ],
        "answer": 0,
        "explanation": "กฎการย่อ IPv6: 1) ตัดเลขศูนย์นำหน้าได้ (เช่น 085B -> 85B, 00A9 -> A9) และ 2) ย่อกลุ่มของ 0000 ที่อยู่ติดกันทั้งหมดเป็น :: ได้เพียงครั้งเดียวในหนึ่งแอดเดรส คำตอบคือ 3FFE:85B:1F1F::A9:1234"
    },
    # Q63
    {
        "id": 63,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address ใน Class A มีช่วงหมายเลขใน Octet แรกเป็นเท่าใด และมี Default Subnet Mask เป็นเท่าใด",
        "options": [
            "0 – 127 และ 255.0.0.0",
            "128 – 191 และ 255.255.0.0",
            "192 – 223 และ 255.255.255.0",
            "224 – 239 และ 255.255.255.255"
        ],
        "answer": 0,
        "explanation": "Class A มีช่วงหมายเลข 0 – 127 (ใช้จริง 1-126) มี Default Subnet Mask คือ 255.0.0.0 (NetID 8 บิต, HostID 24 บิต)"
    },
    # Q64
    {
        "id": 64,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address ใน Class B มีจำนวนบิตที่ใช้เป็น NetID และ HostID อย่างละกี่บิต",
        "options": ["NetID 8 บิต, HostID 24 บิต", "NetID 16 บิต, HostID 16 บิต", "NetID 24 บิต, HostID 8 บิต", "NetID 21 บิต, HostID 11 บิต"],
        "answer": 1,
        "explanation": "Class B มี NetID จำนวน 16 บิต (2 Octets แรก) และ HostID จำนวน 16 บิต (2 Octets หลัง) Default Mask คือ 255.255.0.0"
    },
    # Q65
    {
        "id": 65,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address ใน Class C มีช่วงหมายเลขใน Octet แรกเป็นเท่าใด และรองรับจำนวน Host สูงสุดต่อหนึ่งเครือข่ายกี่โฮสต์",
        "options": ["0 – 127 และ 16,777,214 โฮสต์", "128 – 191 และ 65,534 โฮสต์", "192 – 223 และ 254 โฮสต์", "224 – 239 และ 2 โฮสต์"],
        "answer": 2,
        "explanation": "Class C เริ่มต้นด้วย 192 – 223 มี HostID 8 บิต รองรับ Host ที่ใช้งานได้จริงคือ 2^8 - 2 = 256 - 2 = 254 โฮสต์"
    },
    # Q66
    {
        "id": 66,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address ใน Class D และ Class E ถูกกำหนดไว้เพื่อวัตถุประสงค์ใดตามลำดับ",
        "options": [
            "Class D สำหรับเครือข่ายขนาดใหญ่, Class E สำหรับเครือข่ายขนาดเล็ก",
            "Class D สำหรับการส่งแบบ Multicast, Class E สำหรับสำรองไว้ใช้เพื่อการทดลองและอนาคต",
            "Class D สำหรับเครือข่ายราชการ, Class E สำหรับอินเทอร์เน็ตสาธารณะ",
            "Class D สำหรับเครือข่ายไร้สาย, Class E สำหรับดาวเทียม"
        ],
        "answer": 1,
        "explanation": "Class D (224 – 239) ถูกกำหนดไว้สำหรับกลุ่ม Multicast และ Class E (240 – 255) สำรองไว้สำหรับการทดลองและพัฒนาในอนาคต (Reserved)"
    },
    # Q67
    {
        "id": 67,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address `10.6.5.42` จัดอยู่ใน Class ใด และมี NetID กับ HostID เป็นค่าใด",
        "options": [
            "Class A, NetID = 10, HostID = 6.5.42",
            "Class B, NetID = 10.6, HostID = 5.42",
            "Class C, NetID = 10.6.5, HostID = 42",
            "Class A, NetID = 10.6.5, HostID = 42"
        ],
        "answer": 0,
        "explanation": "Octet แรกคือ 10 จัดอยู่ใน Class A (0-127) ซึ่ง Class A มี NetID 1 Octet (ค่า 10) และ HostID 3 Octets ที่เหลือ (ค่า 6.5.42)"
    },
    # Q68
    {
        "id": 68,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address `128.3.2.3` จัดอยู่ใน Class ใด และมี NetID กับ HostID เป็นค่าใด",
        "options": [
            "Class A, NetID = 128, HostID = 3.2.3",
            "Class B, NetID = 128.3, HostID = 2.3",
            "Class C, NetID = 128.3.2, HostID = 3",
            "Class B, NetID = 128, HostID = 3.2.3"
        ],
        "answer": 1,
        "explanation": "Octet แรกคือ 128 จัดอยู่ใน Class B (128-191) ซึ่ง Class B มี NetID 2 Octets แรก (ค่า 128.3) และ HostID 2 Octets หลัง (ค่า 2.3)"
    },
    # Q69
    {
        "id": 69,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address `193.155.140.10` จัดอยู่ใน Class ใด และมี NetID กับ HostID เป็นค่าใด",
        "options": [
            "Class A, NetID = 193, HostID = 155.140.10",
            "Class B, NetID = 193.155, HostID = 140.10",
            "Class C, NetID = 193.155.140, HostID = 10",
            "Class C, NetID = 193, HostID = 155.140.10"
        ],
        "answer": 2,
        "explanation": "Octet แรกคือ 193 จัดอยู่ใน Class C (192-223) ซึ่ง Class C มี NetID 3 Octets แรก (ค่า 193.155.140) และ HostID 1 Octet สุดท้าย (ค่า 10)"
    },
    # Q70
    {
        "id": 70,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "ค่า Subnet Mask ในรูปแบบเลขฐานสอง `11111111.11111111.11110000.00000000` เมื่อแปลงเป็นเลขฐานสิบ (Dotted-Decimal) จะมีค่าเท่าใด",
        "options": ["255.255.240.0", "255.255.224.0", "255.255.248.0", "255.255.192.0"],
        "answer": 0,
        "explanation": "Octet ที่ 3 คือ 11110000 = 128 + 64 + 32 + 16 = 240 ดังนั้นจะได้ 255.255.240.0"
    },
    # Q71
    {
        "id": 71,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "ค่า Subnet Mask ในรูปแบบเลขฐานสอง `11111111.11111111.11111111.11000000` เมื่อแปลงเป็นเลขฐานสิบ (Dotted-Decimal) จะมีค่าเท่าใด",
        "options": ["255.255.255.128", "255.255.255.192", "255.255.255.224", "255.255.255.240"],
        "answer": 1,
        "explanation": "Octet ที่ 4 มีเลข 1 อยู่สองบิตแรก 11000000 = 128 + 64 = 192 ดังนั้นจะได้ 255.255.255.192"
    },
    # Q72
    {
        "id": 72,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "บริษัท A ต้องการ IP Address 2,000 เลขหมาย โดยกำหนดเริ่มต้นตั้งแต่ `194.56.0.0` ค่า Subnet Mask ที่เหมาะสมที่สุดคือค่าใด",
        "options": ["255.255.240.0", "255.255.248.0", "255.255.252.0", "255.255.254.0"],
        "answer": 1,
        "explanation": "ต้องการ 2,000 เลขหมาย ใช้ 2^11 = 2,048 หมายเลข ดังนั้นต้องมีบิต 0 สำหรับโฮสต์ 11 บิต -> บิต 1 มี 32 - 11 = 21 บิต (/21) คือ 11111111.11111111.11111000.00000000 = 255.255.248.0"
    },
    # Q73
    {
        "id": 73,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "จากข้อที่แล้ว บริษัท A กำหนดเริ่มต้นที่ `194.56.0.0` (ต้องการ 2,000 เลขหมาย, 2^11 = 2,048) หมายเลข IP Address สูงสุด (Broadcast) จะมีค่าเท่าใด",
        "options": ["194.56.1.255", "194.56.3.255", "194.56.7.255", "194.56.15.255"],
        "answer": 2,
        "explanation": "2,048 หมายเลข คิดเป็น 2,048 / 256 = 8 บล็อก (0 ถึง 7 ใน Octet ที่ 3) และ Octet ที่ 4 เป็น 255 ดังนั้น IP สูงสุดคือ 194.56.7.255"
    },
    # Q74
    {
        "id": 74,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "บริษัท B ต้องการ IP Address 500 เลขหมาย โดยเริ่มต้นตั้งแต่ `194.56.0.0` จงหา Subnet Mask และ IP Address สูงสุด",
        "options": [
            "Subnet Mask = 255.255.254.0, IP สูงสุด = 194.56.1.255",
            "Subnet Mask = 255.255.255.0, IP สูงสุด = 194.56.0.255",
            "Subnet Mask = 255.255.252.0, IP สูงสุด = 194.56.3.255",
            "Subnet Mask = 255.255.248.0, IP สูงสุด = 194.56.7.255"
        ],
        "answer": 0,
        "explanation": "ต้องการ 500 เลขหมาย ใช้ 2^9 = 512 หมายเลข มีบิต 0 เท่ากับ 9 บิต -> Mask มี 1 เท่ากับ 23 บิต (/23) = 255.255.254.0 และ IP สูงสุดคือ 194.56.1.255"
    },
    # Q75
    {
        "id": 75,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "บริษัท C ต้องการ IP Address 250 เลขหมาย โดยเริ่มต้นตั้งแต่ `194.56.16.0` จงหา Subnet Mask และ IP Address สูงสุด",
        "options": [
            "Subnet Mask = 255.255.255.0, IP สูงสุด = 194.56.16.255",
            "Subnet Mask = 255.255.255.128, IP สูงสุด = 194.56.16.127",
            "Subnet Mask = 255.255.254.0, IP สูงสุด = 194.56.17.255",
            "Subnet Mask = 255.255.255.192, IP สูงสุด = 194.56.16.63"
        ],
        "answer": 0,
        "explanation": "ต้องการ 250 เลขหมาย ใช้ 2^8 = 256 หมายเลข มีบิต 0 เท่ากับ 8 บิต -> Mask มี 1 เท่ากับ 24 บิต (/24) = 255.255.255.0 และ IP สูงสุดคือ 194.56.16.255"
    },
    # Q76
    {
        "id": 76,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "บริษัท D ต้องการ IP Address 100 เลขหมาย โดยเริ่มต้นตั้งแต่ `194.56.8.0` จงหา Subnet Mask และ IP Address สูงสุด",
        "options": [
            "Subnet Mask = 255.255.255.0, IP สูงสุด = 194.56.8.255",
            "Subnet Mask = 255.255.255.128, IP สูงสุด = 194.56.8.127",
            "Subnet Mask = 255.255.255.192, IP สูงสุด = 194.56.8.63",
            "Subnet Mask = 255.255.255.224, IP สูงสุด = 194.56.8.31"
        ],
        "answer": 1,
        "explanation": "ต้องการ 100 เลขหมาย ใช้ 2^7 = 128 หมายเลข มีบิต 0 เท่ากับ 7 บิต -> Mask มี 1 เท่ากับ 25 บิต (/25) = 255.255.255.128 และ IP สูงสุดคือ 194.56.8.127 (ช่วง 0 ถึง 127)"
    },
    # Q77
    {
        "id": 77,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "ในการคำนวณหาจำนวน Host ที่สามารถนำไปตั้งค่าใช้งานได้จริงต่อหนึ่ง Subnet เหตุใดจึงต้องใช้สูตร 2^H - 2 (ลบออก 2)",
        "options": [
            "ลบค่าของ Router และ Gateway ออกไป",
            "ลบค่า Network Address (IP แรก) และ Broadcast Address (IP สุดท้าย) ออกไป",
            "ลบค่า DNS Server และ DHCP Server ออกไป",
            "เป็นค่าเผื่อความผิดพลาดในการส่งข้อมูล"
        ],
        "answer": 1,
        "explanation": "ต้องลบออก 2 ค่าเสมอ เพราะ IP แรกสุดคือ Network Address (ใช้ระบุเครือข่าย) และ IP ท้ายสุดคือ Broadcast Address (ใช้ส่งข้อมูลถึงทุกโฮสต์) ห้ามนำไปตั้งค่าให้เครื่องคอมพิวเตอร์"
    },
    # Q78
    {
        "id": 78,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หากยืมบิตในส่วนของโฮสต์มาทำเป็น Subnet Bits จำนวน N บิต จะได้จำนวนเครือข่ายย่อย (Subnets) ที่สร้างขึ้นทั้งหมดเท่าใด",
        "options": ["2 * N เครือข่าย", "2^N เครือข่าย", "2^(N - 2) เครือข่าย", "N^2 เครือข่าย"],
        "answer": 1,
        "explanation": "จำนวน Subnet ทั้งหมดคำนวณจากสูตร 2^N เมื่อ N คือจำนวนบิตที่ยืมมาเป็น Subnet Bits"
    },
    # Q79
    {
        "id": 79,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "การกำหนด CIDR Prefix เป็น `/30` จะได้จำนวน Host ที่สามารถนำไปใช้งานได้จริง (Usable Hosts) กี่หมายเลข",
        "options": ["1 หมายเลข", "2 หมายเลข", "4 หมายเลข", "6 หมายเลข"],
        "answer": 1,
        "explanation": "/30 มีบิตโฮสต์เหลือ H = 32 - 30 = 2 บิต จำนวนโฮสต์ที่ใช้ได้จริง = 2^H - 2 = 2^2 - 2 = 4 - 2 = 2 หมายเลข นิยมใช้กับลิงก์เชื่อมต่อระหว่างเราเตอร์ 2 ตัว"
    },
    # Q80
    {
        "id": 80,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "สำหรับหมายเลข IP Address ที่มี Prefix `/28` ค่า Subnet Mask และจำนวน Host ที่ใช้งานได้จริงคือข้อใด",
        "options": [
            "255.255.255.240 และใช้งานได้ 14 โฮสต์",
            "255.255.255.224 และใช้งานได้ 30 โฮสต์",
            "255.255.255.248 และใช้งานได้ 6 โฮสต์",
            "255.255.255.192 และใช้งานได้ 62 โฮสต์"
        ],
        "answer": 0,
        "explanation": "/28 มีบิต 1 จำนวน 28 บิต ใน Octet สุดท้ายมี 1 สี่ตัว (11110000 = 240) ดังนั้น Mask คือ 255.255.255.240 มีบิต 0 เหลือ 4 บิต โฮสต์ที่ใช้ได้ = 2^4 - 2 = 14 โฮสต์"
    },
    # Q81
    {
        "id": 81,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "กำหนด IP Address `192.168.100.25/28` หมายเลข Network Address ของซับเน็ตนี้คือข้อใด",
        "options": ["192.168.100.0", "192.168.100.16", "192.168.100.24", "192.168.100.32"],
        "answer": 1,
        "explanation": "/28 มี Block size = 256 - 240 = 16 พหุคูณของ 16 ที่ไม่เกิน 25 คือ 16 ดังนั้น Network Address คือ 192.168.100.16"
    },
    # Q82
    {
        "id": 82,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "จากข้อที่แล้ว IP Address `192.168.100.25/28` จะมี Broadcast Address และช่วงโฮสต์ที่ใช้งานได้จริงเป็นข้อใด",
        "options": [
            "Broadcast = 192.168.100.31, ช่วงโฮสต์ = 192.168.100.17 – 192.168.100.30",
            "Broadcast = 192.168.100.32, ช่วงโฮสต์ = 192.168.100.16 – 192.168.100.31",
            "Broadcast = 192.168.100.255, ช่วงโฮสต์ = 192.168.100.1 – 192.168.100.254",
            "Broadcast = 192.168.100.28, ช่วงโฮสต์ = 192.168.100.25 – 192.168.100.27"
        ],
        "answer": 0,
        "explanation": "Network Address คือ .16 มี Block size 16 ดังนั้น Broadcast Address คือ 16 + 16 - 1 = 192.168.100.31 ช่วงที่ใช้งานได้คือ 192.168.100.17 ถึง 192.168.100.30"
    },
    # Q83
    {
        "id": 83,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "กำหนด IP Address `172.30.10.130/30` จะมี Network Address และ Broadcast Address เป็นค่าใด",
        "options": [
            "Network = 172.30.10.128, Broadcast = 172.30.10.131",
            "Network = 172.30.10.130, Broadcast = 172.30.10.133",
            "Network = 172.30.10.0, Broadcast = 172.30.10.255",
            "Network = 172.30.10.128, Broadcast = 172.30.10.255"
        ],
        "answer": 0,
        "explanation": "/30 มี Block size = 4 พหุคูณของ 4 ที่ไม่เกิน 130 คือ 128 ดังนั้น Network Address คือ 172.30.10.128 และ Broadcast Address คือ 128 + 4 - 1 = 172.30.10.131"
    },
    # Q84
    {
        "id": 84,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "กำหนด IP Address `10.1.113.75/19` หมายเลข Network Address ของซับเน็ตนี้คือข้อใด",
        "options": ["10.1.0.0", "10.1.64.0", "10.1.96.0", "10.1.112.0"],
        "answer": 2,
        "explanation": "/19 อยู่ใน Octet ที่ 3 (8+8+3 บิต) Mask คือ 255.255.224.0 มี Block size ใน Octet 3 เท่ากับ 256 - 224 = 32 พหุคูณของ 32 ไม่เกิน 113 คือ (0, 32, 64, 96, 128) -> ได้ 96 ดังนั้น Network Address คือ 10.1.96.0"
    },
    # Q85
    {
        "id": 85,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "จากข้อที่แล้ว IP Address `10.1.113.75/19` จะมี Broadcast Address และจำนวน Host ที่ใช้งานได้จริงเท่าใด",
        "options": [
            "Broadcast = 10.1.127.255, จำนวนโฮสต์ = 8,190 ตัว",
            "Broadcast = 10.1.113.255, จำนวนโฮสต์ = 510 ตัว",
            "Broadcast = 10.1.255.255, จำนวนโฮสต์ = 65,534 ตัว",
            "Broadcast = 10.1.128.0, จำนวนโฮสต์ = 8,192 ตัว"
        ],
        "answer": 0,
        "explanation": "Octet 3 มีค่า 96 + 32 - 1 = 127 และ Octet 4 เต็ม 255 ดังนั้น Broadcast Address คือ 10.1.127.255 บิตโฮสต์เหลือ H = 32 - 19 = 13 บิต โฮสต์ที่ใช้ได้ = 2^13 - 2 = 8,192 - 2 = 8,190 ตัว"
    },
    # Q86
    {
        "id": 86,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "กำหนด IP Address `128.107.14.191/22` จะมี Network Address และ Broadcast Address เป็นค่าใด",
        "options": [
            "Network = 128.107.12.0, Broadcast = 128.107.15.255",
            "Network = 128.107.14.0, Broadcast = 128.107.14.255",
            "Network = 128.107.0.0, Broadcast = 128.107.255.255",
            "Network = 128.107.12.0, Broadcast = 128.107.12.255"
        ],
        "answer": 0,
        "explanation": "/22 ตกใน Octet ที่ 3 (8+8+6 บิต) Mask คือ 255.255.252.0 Block size ใน Octet 3 = 256 - 252 = 4 พหุคูณของ 4 ที่ไม่เกิน 14 คือ 12 ดังนั้น Network Address คือ 128.107.12.0 และ Broadcast คือ 12 + 4 - 1 = 15 ใน Octet 3 -> 128.107.15.255"
    },
    # Q87
    {
        "id": 87,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "หมายเลข IP Address `10.10.10.0/13` สามารถนำไปกำหนดเป็นหมายเลขโฮสต์ (Host IP) ให้กับเครื่องคอมพิวเตอร์ได้หรือไม่ เพราะเหตุใด",
        "options": [
            "ไม่ได้ เพราะลงท้ายด้วยเลข 0 ซึ่งต้องเป็น Network Address เสมอ",
            "ได้ เพราะสำหรับ /13 ช่วง Network คือ 10.8.0.0 และ Broadcast คือ 10.15.255.255 ทำให้ 10.10.10.0 เป็นโฮสต์ที่อยู่ในช่วงใช้งานได้",
            "ไม่ได้ เพราะเป็น Class A ที่ไม่สามารถแบ่งซับเน็ตได้",
            "ได้ แต่ต้องได้รับอนุญาตจาก ISP ก่อนเท่านั้น"
        ],
        "answer": 1,
        "explanation": "/13 ตกใน Octet ที่ 2 (บิตที่ 9-13 มี 5 บิต -> Mask 255.248.0.0, Block size = 32) Network คือ 10.8.0.0 และ Broadcast คือ 10.15.255.255 ช่วงโฮสต์ที่ใช้ได้คือ 10.8.0.1 - 10.15.255.254 ดังนั้น 10.10.10.0 จึงเป็น IP ที่นำไปเซ็ตให้โฮสต์ได้ปกติ (แม้จะลงท้ายด้วย .0)"
    },
    # Q88
    {
        "id": 88,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "ในโปรแกรม Cisco Packet Tracer สัญลักษณ์รูปทรงกระบอกกลมที่มีลูกศร 4 ทิศทางชี้เข้าหากันและชี้ออก แทนอุปกรณ์เครือข่ายชนิดใด",
        "options": ["Router", "Switch", "Hub", "Access Point"],
        "answer": 0,
        "explanation": "สัญลักษณ์ทรงกระบอกกลมมีลูกศร 4 ทิศทางใน Cisco Packet Tracer คือ 'Router' (ทำหน้าที่หาเส้นทางและส่งต่อแพ็กเก็ตใน Layer 3)"
    },
    # Q89
    {
        "id": 89,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "ในโปรแกรม Cisco Packet Tracer สัญลักษณ์กล่องสี่เหลี่ยมที่มีลูกศร 4 เส้นวิ่งสวนทางกันซ้าย-ขวา แทนอุปกรณ์เครือข่ายชนิดใด",
        "options": ["Hub", "Switch", "Router", "Server"],
        "answer": 1,
        "explanation": "สัญลักษณ์กล่องสี่เหลี่ยมลูกศร 4 เส้นวิ่งสวนทางกันซ้าย-ขวา คือ 'Switch' (ทำหน้าที่สลับสายและส่งต่อข้อมูลใน Layer 2)"
    },
    # Q90
    {
        "id": 90,
        "chapter": "บทที่ 8: Subnetting & IP Addressing",
        "question": "ในโปรแกรม Cisco Packet Tracer สัญลักษณ์รูปก้อนเมฆ (Network Cloud) มักถูกนำมาใช้เพื่อเป็นตัวแทนของอะไรในการจำลองระบบ",
        "options": [
            "เครือข่ายภายนอกวงกว้าง เช่น WAN หรือ อินเทอร์เน็ต (Internet)",
            "ศูนย์เก็บข้อมูล Cloud Storage ภายในเครื่อง",
            "ระบบสัญญาณสภาพอากาศ",
            "เครื่องคอมพิวเตอร์แม่ข่ายจำลอง"
        ],
        "answer": 0,
        "explanation": "Network Cloud ในแบบจำลองเครือข่ายเป็นตัวแทนของเครือข่ายภายนอกวงกว้าง เช่น WAN, Frame Relay หรือ อินเทอร์เน็ต (Internet)"
    }
]

# Write to data/questions90.js
questions_path = os.path.join(data_dir, "questions90.js")
with open(questions_path, "w", encoding="utf-8") as f:
    f.write("// Final Exam 90 Questions for COM2703 (Chapters 5-8)\n")
    f.write("window.QUESTIONS_90 = ")
    json.dump(questions, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Generated data/questions90.js successfully ({len(questions)} questions)!")
