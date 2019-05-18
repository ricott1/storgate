HASH_TABLE = (
    {'code': 0x0, 'hash': 'id'},
    {'code': 0x11, 'length': 0x14, 'hash': 'sha1'},
    {'code': 0x12, 'length': 0x20, 'hash': 'sha2-256'},
    {'code': 0x13, 'length': 0x40, 'hash': 'sha2-512'},
    {'code': 0x14, 'length': 0x40, 'hash': 'sha3-512'},
    {'code': 0x15, 'length': 0x30, 'hash': 'sha3-384'},
    {'code': 0x16, 'length': 0x20, 'hash': 'sha3-256'},
    {'code': 0x17, 'length': 0x1c, 'hash': 'sha3-224'},
    {'code': 0x18, 'length': 0x20, 'hash': 'shake-128'},
    {'code': 0x19, 'length': 0x40, 'hash': 'shake-256'},
    {'code': 0x1a, 'length': 0x1c, 'hash': 'keccak-224'},
    {'code': 0x1b, 'length': 0x20, 'hash': 'keccak-256'},
    {'code': 0x1c, 'length': 0x30, 'hash': 'keccak-384'},
    {'code': 0x1d, 'length': 0x40, 'hash': 'keccak-512'},
    {'code': 0x22, 'length': 0x20, 'hash': 'murmur3-128'},
    {'code': 0x23, 'hash': 'murmur3-32'},
    {'code': 0x56, 'length': 0x20, 'hash': 'dbl-sha2-256'},
    {'code': 0xb201, 'length': 0x1, 'hash': 'blake2b-8'},
    {'code': 0xb202, 'length': 0x2, 'hash': 'blake2b-16'},
    {'code': 0xb203, 'length': 0x3, 'hash': 'blake2b-24'},
    {'code': 0xb204, 'length': 0x4, 'hash': 'blake2b-32'},
    {'code': 0xb205, 'length': 0x5, 'hash': 'blake2b-40'},
    {'code': 0xb206, 'length': 0x6, 'hash': 'blake2b-48'},
    {'code': 0xb207, 'length': 0x7, 'hash': 'blake2b-56'},
    {'code': 0xb208, 'length': 0x8, 'hash': 'blake2b-64'},
    {'code': 0xb209, 'length': 0x9, 'hash': 'blake2b-72'},
    {'code': 0xb20a, 'length': 0xa, 'hash': 'blake2b-80'},
    {'code': 0xb20b, 'length': 0xb, 'hash': 'blake2b-88'},
    {'code': 0xb20c, 'length': 0xc, 'hash': 'blake2b-96'},
    {'code': 0xb20d, 'length': 0xd, 'hash': 'blake2b-104'},
    {'code': 0xb20e, 'length': 0xe, 'hash': 'blake2b-112'},
    {'code': 0xb20f, 'length': 0xf, 'hash': 'blake2b-120'},
    {'code': 0xb210, 'length': 0x10, 'hash': 'blake2b-128'},
    {'code': 0xb211, 'length': 0x11, 'hash': 'blake2b-136'},
    {'code': 0xb212, 'length': 0x12, 'hash': 'blake2b-144'},
    {'code': 0xb213, 'length': 0x13, 'hash': 'blake2b-152'},
    {'code': 0xb214, 'length': 0x14, 'hash': 'blake2b-160'},
    {'code': 0xb215, 'length': 0x15, 'hash': 'blake2b-168'},
    {'code': 0xb216, 'length': 0x16, 'hash': 'blake2b-176'},
    {'code': 0xb217, 'length': 0x17, 'hash': 'blake2b-184'},
    {'code': 0xb218, 'length': 0x18, 'hash': 'blake2b-192'},
    {'code': 0xb219, 'length': 0x19, 'hash': 'blake2b-200'},
    {'code': 0xb21a, 'length': 0x1a, 'hash': 'blake2b-208'},
    {'code': 0xb21b, 'length': 0x1b, 'hash': 'blake2b-216'},
    {'code': 0xb21c, 'length': 0x1c, 'hash': 'blake2b-224'},
    {'code': 0xb21d, 'length': 0x1d, 'hash': 'blake2b-232'},
    {'code': 0xb21e, 'length': 0x1e, 'hash': 'blake2b-240'},
    {'code': 0xb21f, 'length': 0x1f, 'hash': 'blake2b-248'},
    {'code': 0xb220, 'length': 0x20, 'hash': 'blake2b-256'},
    {'code': 0xb221, 'length': 0x21, 'hash': 'blake2b-264'},
    {'code': 0xb222, 'length': 0x22, 'hash': 'blake2b-272'},
    {'code': 0xb223, 'length': 0x23, 'hash': 'blake2b-280'},
    {'code': 0xb224, 'length': 0x24, 'hash': 'blake2b-288'},
    {'code': 0xb225, 'length': 0x25, 'hash': 'blake2b-296'},
    {'code': 0xb226, 'length': 0x26, 'hash': 'blake2b-304'},
    {'code': 0xb227, 'length': 0x27, 'hash': 'blake2b-312'},
    {'code': 0xb228, 'length': 0x28, 'hash': 'blake2b-320'},
    {'code': 0xb229, 'length': 0x29, 'hash': 'blake2b-328'},
    {'code': 0xb22a, 'length': 0x2a, 'hash': 'blake2b-336'},
    {'code': 0xb22b, 'length': 0x2b, 'hash': 'blake2b-344'},
    {'code': 0xb22c, 'length': 0x2c, 'hash': 'blake2b-352'},
    {'code': 0xb22d, 'length': 0x2d, 'hash': 'blake2b-360'},
    {'code': 0xb22e, 'length': 0x2e, 'hash': 'blake2b-368'},
    {'code': 0xb22f, 'length': 0x2f, 'hash': 'blake2b-376'},
    {'code': 0xb230, 'length': 0x30, 'hash': 'blake2b-384'},
    {'code': 0xb231, 'length': 0x31, 'hash': 'blake2b-392'},
    {'code': 0xb232, 'length': 0x32, 'hash': 'blake2b-400'},
    {'code': 0xb233, 'length': 0x33, 'hash': 'blake2b-408'},
    {'code': 0xb234, 'length': 0x34, 'hash': 'blake2b-416'},
    {'code': 0xb235, 'length': 0x35, 'hash': 'blake2b-424'},
    {'code': 0xb236, 'length': 0x36, 'hash': 'blake2b-432'},
    {'code': 0xb237, 'length': 0x37, 'hash': 'blake2b-440'},
    {'code': 0xb238, 'length': 0x38, 'hash': 'blake2b-448'},
    {'code': 0xb239, 'length': 0x39, 'hash': 'blake2b-456'},
    {'code': 0xb23a, 'length': 0x3a, 'hash': 'blake2b-464'},
    {'code': 0xb23b, 'length': 0x3b, 'hash': 'blake2b-472'},
    {'code': 0xb23c, 'length': 0x3c, 'hash': 'blake2b-480'},
    {'code': 0xb23d, 'length': 0x3d, 'hash': 'blake2b-488'},
    {'code': 0xb23e, 'length': 0x3e, 'hash': 'blake2b-496'},
    {'code': 0xb23f, 'length': 0x3f, 'hash': 'blake2b-504'},
    {'code': 0xb240, 'length': 0x40, 'hash': 'blake2b-512'},
    {'code': 0xb241, 'length': 0x1, 'hash': 'blake2s-8'},
    {'code': 0xb242, 'length': 0x2, 'hash': 'blake2s-16'},
    {'code': 0xb243, 'length': 0x3, 'hash': 'blake2s-24'},
    {'code': 0xb244, 'length': 0x4, 'hash': 'blake2s-32'},
    {'code': 0xb245, 'length': 0x5, 'hash': 'blake2s-40'},
    {'code': 0xb246, 'length': 0x6, 'hash': 'blake2s-48'},
    {'code': 0xb247, 'length': 0x7, 'hash': 'blake2s-56'},
    {'code': 0xb248, 'length': 0x8, 'hash': 'blake2s-64'},
    {'code': 0xb249, 'length': 0x9, 'hash': 'blake2s-72'},
    {'code': 0xb24a, 'length': 0xa, 'hash': 'blake2s-80'},
    {'code': 0xb24b, 'length': 0xb, 'hash': 'blake2s-88'},
    {'code': 0xb24c, 'length': 0xc, 'hash': 'blake2s-96'},
    {'code': 0xb24d, 'length': 0xd, 'hash': 'blake2s-104'},
    {'code': 0xb24e, 'length': 0xe, 'hash': 'blake2s-112'},
    {'code': 0xb24f, 'length': 0xf, 'hash': 'blake2s-120'},
    {'code': 0xb250, 'length': 0x10, 'hash': 'blake2s-128'},
    {'code': 0xb251, 'length': 0x11, 'hash': 'blake2s-136'},
    {'code': 0xb252, 'length': 0x12, 'hash': 'blake2s-144'},
    {'code': 0xb253, 'length': 0x13, 'hash': 'blake2s-152'},
    {'code': 0xb254, 'length': 0x14, 'hash': 'blake2s-160'},
    {'code': 0xb255, 'length': 0x15, 'hash': 'blake2s-168'},
    {'code': 0xb256, 'length': 0x16, 'hash': 'blake2s-176'},
    {'code': 0xb257, 'length': 0x17, 'hash': 'blake2s-184'},
    {'code': 0xb258, 'length': 0x18, 'hash': 'blake2s-192'},
    {'code': 0xb259, 'length': 0x19, 'hash': 'blake2s-200'},
    {'code': 0xb25a, 'length': 0x1a, 'hash': 'blake2s-208'},
    {'code': 0xb25b, 'length': 0x1b, 'hash': 'blake2s-216'},
    {'code': 0xb25c, 'length': 0x1c, 'hash': 'blake2s-224'},
    {'code': 0xb25d, 'length': 0x1d, 'hash': 'blake2s-232'},
    {'code': 0xb25e, 'length': 0x1e, 'hash': 'blake2s-240'},
    {'code': 0xb25f, 'length': 0x1f, 'hash': 'blake2s-248'},
    {'code': 0xb260, 'length': 0x20, 'hash': 'blake2s-256'},
    {'code': 0x01bc, 'length': 0xa, 'hash': 'onion'},
    {'code': 0x01bd, 'length': 0x23, 'hash': 'onion3'},
    {'code': 0xb301, 'length': 0x1, 'hash': 'Skein256-8'},
    {'code': 0xb302, 'length': 0x2, 'hash': 'Skein256-16'},
    {'code': 0xb303, 'length': 0x3, 'hash': 'Skein256-24'},
    {'code': 0xb304, 'length': 0x4, 'hash': 'Skein256-32'},
    {'code': 0xb305, 'length': 0x5, 'hash': 'Skein256-40'},
    {'code': 0xb306, 'length': 0x6, 'hash': 'Skein256-48'},
    {'code': 0xb307, 'length': 0x7, 'hash': 'Skein256-56'},
    {'code': 0xb308, 'length': 0x8, 'hash': 'Skein256-64'},
    {'code': 0xb309, 'length': 0x9, 'hash': 'Skein256-72'},
    {'code': 0xb30a, 'length': 0xa, 'hash': 'Skein256-80'},
    {'code': 0xb30b, 'length': 0xb, 'hash': 'Skein256-88'},
    {'code': 0xb30c, 'length': 0xc, 'hash': 'Skein256-96'},
    {'code': 0xb30d, 'length': 0xd, 'hash': 'Skein256-104'},
    {'code': 0xb30e, 'length': 0xe, 'hash': 'Skein256-112'},
    {'code': 0xb30f, 'length': 0xf, 'hash': 'Skein256-120'},
    {'code': 0xb310, 'length': 0x10, 'hash': 'Skein256-128'},
    {'code': 0xb311, 'length': 0x11, 'hash': 'Skein256-136'},
    {'code': 0xb312, 'length': 0x12, 'hash': 'Skein256-144'},
    {'code': 0xb313, 'length': 0x13, 'hash': 'Skein256-152'},
    {'code': 0xb314, 'length': 0x14, 'hash': 'Skein256-160'},
    {'code': 0xb315, 'length': 0x15, 'hash': 'Skein256-168'},
    {'code': 0xb316, 'length': 0x16, 'hash': 'Skein256-176'},
    {'code': 0xb317, 'length': 0x17, 'hash': 'Skein256-184'},
    {'code': 0xb318, 'length': 0x18, 'hash': 'Skein256-192'},
    {'code': 0xb319, 'length': 0x19, 'hash': 'Skein256-200'},
    {'code': 0xb31a, 'length': 0x1a, 'hash': 'Skein256-208'},
    {'code': 0xb31b, 'length': 0x1b, 'hash': 'Skein256-216'},
    {'code': 0xb31c, 'length': 0x1c, 'hash': 'Skein256-224'},
    {'code': 0xb31d, 'length': 0x1d, 'hash': 'Skein256-232'},
    {'code': 0xb31e, 'length': 0x1e, 'hash': 'Skein256-240'},
    {'code': 0xb31f, 'length': 0x1f, 'hash': 'Skein256-248'},
    {'code': 0xb320, 'length': 0x20, 'hash': 'Skein256-256'},
    {'code': 0xb321, 'length': 0x1, 'hash': 'Skein512-8'},
    {'code': 0xb322, 'length': 0x2, 'hash': 'Skein512-16'},
    {'code': 0xb323, 'length': 0x3, 'hash': 'Skein512-24'},
    {'code': 0xb324, 'length': 0x4, 'hash': 'Skein512-32'},
    {'code': 0xb325, 'length': 0x5, 'hash': 'Skein512-40'},
    {'code': 0xb326, 'length': 0x6, 'hash': 'Skein512-48'},
    {'code': 0xb327, 'length': 0x7, 'hash': 'Skein512-56'},
    {'code': 0xb328, 'length': 0x8, 'hash': 'Skein512-64'},
    {'code': 0xb329, 'length': 0x9, 'hash': 'Skein512-72'},
    {'code': 0xb32a, 'length': 0xa, 'hash': 'Skein512-80'},
    {'code': 0xb32b, 'length': 0xb, 'hash': 'Skein512-88'},
    {'code': 0xb32c, 'length': 0xc, 'hash': 'Skein512-96'},
    {'code': 0xb32d, 'length': 0xd, 'hash': 'Skein512-104'},
    {'code': 0xb32e, 'length': 0xe, 'hash': 'Skein512-112'},
    {'code': 0xb32f, 'length': 0xf, 'hash': 'Skein512-120'},
    {'code': 0xb330, 'length': 0x10, 'hash': 'Skein512-128'},
    {'code': 0xb331, 'length': 0x11, 'hash': 'Skein512-136'},
    {'code': 0xb332, 'length': 0x12, 'hash': 'Skein512-144'},
    {'code': 0xb333, 'length': 0x13, 'hash': 'Skein512-152'},
    {'code': 0xb334, 'length': 0x14, 'hash': 'Skein512-160'},
    {'code': 0xb335, 'length': 0x15, 'hash': 'Skein512-168'},
    {'code': 0xb336, 'length': 0x16, 'hash': 'Skein512-176'},
    {'code': 0xb337, 'length': 0x17, 'hash': 'Skein512-184'},
    {'code': 0xb338, 'length': 0x18, 'hash': 'Skein512-192'},
    {'code': 0xb339, 'length': 0x19, 'hash': 'Skein512-200'},
    {'code': 0xb33a, 'length': 0x1a, 'hash': 'Skein512-208'},
    {'code': 0xb33b, 'length': 0x1b, 'hash': 'Skein512-216'},
    {'code': 0xb33c, 'length': 0x1c, 'hash': 'Skein512-224'},
    {'code': 0xb33d, 'length': 0x1d, 'hash': 'Skein512-232'},
    {'code': 0xb33e, 'length': 0x1e, 'hash': 'Skein512-240'},
    {'code': 0xb33f, 'length': 0x1f, 'hash': 'Skein512-248'},
    {'code': 0xb340, 'length': 0x20, 'hash': 'Skein512-256'},
    {'code': 0xb341, 'length': 0x21, 'hash': 'Skein512-264'},
    {'code': 0xb342, 'length': 0x22, 'hash': 'Skein512-272'},
    {'code': 0xb343, 'length': 0x23, 'hash': 'Skein512-280'},
    {'code': 0xb344, 'length': 0x24, 'hash': 'Skein512-288'},
    {'code': 0xb345, 'length': 0x25, 'hash': 'Skein512-296'},
    {'code': 0xb346, 'length': 0x26, 'hash': 'Skein512-304'},
    {'code': 0xb347, 'length': 0x27, 'hash': 'Skein512-312'},
    {'code': 0xb348, 'length': 0x28, 'hash': 'Skein512-320'},
    {'code': 0xb349, 'length': 0x29, 'hash': 'Skein512-328'},
    {'code': 0xb34a, 'length': 0x2a, 'hash': 'Skein512-336'},
    {'code': 0xb34b, 'length': 0x2b, 'hash': 'Skein512-344'},
    {'code': 0xb34c, 'length': 0x2c, 'hash': 'Skein512-352'},
    {'code': 0xb34d, 'length': 0x2d, 'hash': 'Skein512-360'},
    {'code': 0xb34e, 'length': 0x2e, 'hash': 'Skein512-368'},
    {'code': 0xb34f, 'length': 0x2f, 'hash': 'Skein512-376'},
    {'code': 0xb350, 'length': 0x30, 'hash': 'Skein512-384'},
    {'code': 0xb351, 'length': 0x31, 'hash': 'Skein512-392'},
    {'code': 0xb352, 'length': 0x32, 'hash': 'Skein512-400'},
    {'code': 0xb353, 'length': 0x33, 'hash': 'Skein512-408'},
    {'code': 0xb354, 'length': 0x34, 'hash': 'Skein512-416'},
    {'code': 0xb355, 'length': 0x35, 'hash': 'Skein512-424'},
    {'code': 0xb356, 'length': 0x36, 'hash': 'Skein512-432'},
    {'code': 0xb357, 'length': 0x37, 'hash': 'Skein512-440'},
    {'code': 0xb358, 'length': 0x38, 'hash': 'Skein512-448'},
    {'code': 0xb359, 'length': 0x39, 'hash': 'Skein512-456'},
    {'code': 0xb35a, 'length': 0x3a, 'hash': 'Skein512-464'},
    {'code': 0xb35b, 'length': 0x3b, 'hash': 'Skein512-472'},
    {'code': 0xb35c, 'length': 0x3c, 'hash': 'Skein512-480'},
    {'code': 0xb35d, 'length': 0x3d, 'hash': 'Skein512-488'},
    {'code': 0xb35e, 'length': 0x3e, 'hash': 'Skein512-496'},
    {'code': 0xb35f, 'length': 0x3f, 'hash': 'Skein512-504'},
    {'code': 0xb360, 'length': 0x40, 'hash': 'Skein512-512'},
    {'code': 0xb361, 'length': 0x1, 'hash': 'Skein1024-8'},
    {'code': 0xb362, 'length': 0x2, 'hash': 'Skein1024-16'},
    {'code': 0xb363, 'length': 0x3, 'hash': 'Skein1024-24'},
    {'code': 0xb364, 'length': 0x4, 'hash': 'Skein1024-32'},
    {'code': 0xb365, 'length': 0x5, 'hash': 'Skein1024-40'},
    {'code': 0xb366, 'length': 0x6, 'hash': 'Skein1024-48'},
    {'code': 0xb367, 'length': 0x7, 'hash': 'Skein1024-56'},
    {'code': 0xb368, 'length': 0x8, 'hash': 'Skein1024-64'},
    {'code': 0xb369, 'length': 0x9, 'hash': 'Skein1024-72'},
    {'code': 0xb36a, 'length': 0xa, 'hash': 'Skein1024-80'},
    {'code': 0xb36b, 'length': 0xb, 'hash': 'Skein1024-88'},
    {'code': 0xb36c, 'length': 0xc, 'hash': 'Skein1024-96'},
    {'code': 0xb36d, 'length': 0xd, 'hash': 'Skein1024-104'},
    {'code': 0xb36e, 'length': 0xe, 'hash': 'Skein1024-112'},
    {'code': 0xb36f, 'length': 0xf, 'hash': 'Skein1024-120'},
    {'code': 0xb370, 'length': 0x10, 'hash': 'Skein1024-128'},
    {'code': 0xb371, 'length': 0x11, 'hash': 'Skein1024-136'},
    {'code': 0xb372, 'length': 0x12, 'hash': 'Skein1024-144'},
    {'code': 0xb373, 'length': 0x13, 'hash': 'Skein1024-152'},
    {'code': 0xb374, 'length': 0x14, 'hash': 'Skein1024-160'},
    {'code': 0xb375, 'length': 0x15, 'hash': 'Skein1024-168'},
    {'code': 0xb376, 'length': 0x16, 'hash': 'Skein1024-176'},
    {'code': 0xb377, 'length': 0x17, 'hash': 'Skein1024-184'},
    {'code': 0xb378, 'length': 0x18, 'hash': 'Skein1024-192'},
    {'code': 0xb379, 'length': 0x19, 'hash': 'Skein1024-200'},
    {'code': 0xb37a, 'length': 0x1a, 'hash': 'Skein1024-208'},
    {'code': 0xb37b, 'length': 0x1b, 'hash': 'Skein1024-216'},
    {'code': 0xb37c, 'length': 0x1c, 'hash': 'Skein1024-224'},
    {'code': 0xb37d, 'length': 0x1d, 'hash': 'Skein1024-232'},
    {'code': 0xb37e, 'length': 0x1e, 'hash': 'Skein1024-240'},
    {'code': 0xb37f, 'length': 0x1f, 'hash': 'Skein1024-248'},
    {'code': 0xb380, 'length': 0x20, 'hash': 'Skein1024-256'},
    {'code': 0xb381, 'length': 0x21, 'hash': 'Skein1024-264'},
    {'code': 0xb382, 'length': 0x22, 'hash': 'Skein1024-272'},
    {'code': 0xb383, 'length': 0x23, 'hash': 'Skein1024-280'},
    {'code': 0xb384, 'length': 0x24, 'hash': 'Skein1024-288'},
    {'code': 0xb385, 'length': 0x25, 'hash': 'Skein1024-296'},
    {'code': 0xb386, 'length': 0x26, 'hash': 'Skein1024-304'},
    {'code': 0xb387, 'length': 0x27, 'hash': 'Skein1024-312'},
    {'code': 0xb388, 'length': 0x28, 'hash': 'Skein1024-320'},
    {'code': 0xb389, 'length': 0x29, 'hash': 'Skein1024-328'},
    {'code': 0xb38a, 'length': 0x2a, 'hash': 'Skein1024-336'},
    {'code': 0xb38b, 'length': 0x2b, 'hash': 'Skein1024-344'},
    {'code': 0xb38c, 'length': 0x2c, 'hash': 'Skein1024-352'},
    {'code': 0xb38d, 'length': 0x2d, 'hash': 'Skein1024-360'},
    {'code': 0xb38e, 'length': 0x2e, 'hash': 'Skein1024-368'},
    {'code': 0xb38f, 'length': 0x2f, 'hash': 'Skein1024-376'},
    {'code': 0xb390, 'length': 0x30, 'hash': 'Skein1024-384'},
    {'code': 0xb391, 'length': 0x31, 'hash': 'Skein1024-392'},
    {'code': 0xb392, 'length': 0x32, 'hash': 'Skein1024-400'},
    {'code': 0xb393, 'length': 0x33, 'hash': 'Skein1024-408'},
    {'code': 0xb394, 'length': 0x34, 'hash': 'Skein1024-416'},
    {'code': 0xb395, 'length': 0x35, 'hash': 'Skein1024-424'},
    {'code': 0xb396, 'length': 0x36, 'hash': 'Skein1024-432'},
    {'code': 0xb397, 'length': 0x37, 'hash': 'Skein1024-440'},
    {'code': 0xb398, 'length': 0x38, 'hash': 'Skein1024-448'},
    {'code': 0xb399, 'length': 0x39, 'hash': 'Skein1024-456'},
    {'code': 0xb39a, 'length': 0x3a, 'hash': 'Skein1024-464'},
    {'code': 0xb39b, 'length': 0x3b, 'hash': 'Skein1024-472'},
    {'code': 0xb39c, 'length': 0x3c, 'hash': 'Skein1024-480'},
    {'code': 0xb39d, 'length': 0x3d, 'hash': 'Skein1024-488'},
    {'code': 0xb39e, 'length': 0x3e, 'hash': 'Skein1024-496'},
    {'code': 0xb39f, 'length': 0x3f, 'hash': 'Skein1024-504'},
    {'code': 0xb3a0, 'length': 0x40, 'hash': 'Skein1024-512'},
    {'code': 0xb3a1, 'length': 0x41, 'hash': 'Skein1024-520'},
    {'code': 0xb3a2, 'length': 0x42, 'hash': 'Skein1024-528'},
    {'code': 0xb3a3, 'length': 0x43, 'hash': 'Skein1024-536'},
    {'code': 0xb3a4, 'length': 0x44, 'hash': 'Skein1024-544'},
    {'code': 0xb3a5, 'length': 0x45, 'hash': 'Skein1024-552'},
    {'code': 0xb3a6, 'length': 0x46, 'hash': 'Skein1024-560'},
    {'code': 0xb3a7, 'length': 0x47, 'hash': 'Skein1024-568'},
    {'code': 0xb3a8, 'length': 0x48, 'hash': 'Skein1024-576'},
    {'code': 0xb3a9, 'length': 0x49, 'hash': 'Skein1024-584'},
    {'code': 0xb3aa, 'length': 0x4a, 'hash': 'Skein1024-592'},
    {'code': 0xb3ab, 'length': 0x4b, 'hash': 'Skein1024-600'},
    {'code': 0xb3ac, 'length': 0x4c, 'hash': 'Skein1024-608'},
    {'code': 0xb3ad, 'length': 0x4d, 'hash': 'Skein1024-616'},
    {'code': 0xb3ae, 'length': 0x4e, 'hash': 'Skein1024-624'},
    {'code': 0xb3af, 'length': 0x4f, 'hash': 'Skein1024-632'},
    {'code': 0xb3b0, 'length': 0x50, 'hash': 'Skein1024-640'},
    {'code': 0xb3b1, 'length': 0x51, 'hash': 'Skein1024-648'},
    {'code': 0xb3b2, 'length': 0x52, 'hash': 'Skein1024-656'},
    {'code': 0xb3b3, 'length': 0x53, 'hash': 'Skein1024-664'},
    {'code': 0xb3b4, 'length': 0x54, 'hash': 'Skein1024-672'},
    {'code': 0xb3b5, 'length': 0x55, 'hash': 'Skein1024-680'},
    {'code': 0xb3b6, 'length': 0x56, 'hash': 'Skein1024-688'},
    {'code': 0xb3b7, 'length': 0x57, 'hash': 'Skein1024-696'},
    {'code': 0xb3b8, 'length': 0x58, 'hash': 'Skein1024-704'},
    {'code': 0xb3b9, 'length': 0x59, 'hash': 'Skein1024-712'},
    {'code': 0xb3ba, 'length': 0x5a, 'hash': 'Skein1024-720'},
    {'code': 0xb3bb, 'length': 0x5b, 'hash': 'Skein1024-728'},
    {'code': 0xb3bc, 'length': 0x5c, 'hash': 'Skein1024-736'},
    {'code': 0xb3bd, 'length': 0x5d, 'hash': 'Skein1024-744'},
    {'code': 0xb3be, 'length': 0x5e, 'hash': 'Skein1024-752'},
    {'code': 0xb3bf, 'length': 0x5f, 'hash': 'Skein1024-760'},
    {'code': 0xb3c0, 'length': 0x60, 'hash': 'Skein1024-768'},
    {'code': 0xb3c1, 'length': 0x61, 'hash': 'Skein1024-776'},
    {'code': 0xb3c2, 'length': 0x62, 'hash': 'Skein1024-784'},
    {'code': 0xb3c3, 'length': 0x63, 'hash': 'Skein1024-792'},
    {'code': 0xb3c4, 'length': 0x64, 'hash': 'Skein1024-800'},
    {'code': 0xb3c5, 'length': 0x65, 'hash': 'Skein1024-808'},
    {'code': 0xb3c6, 'length': 0x66, 'hash': 'Skein1024-816'},
    {'code': 0xb3c7, 'length': 0x67, 'hash': 'Skein1024-824'},
    {'code': 0xb3c8, 'length': 0x68, 'hash': 'Skein1024-832'},
    {'code': 0xb3c9, 'length': 0x69, 'hash': 'Skein1024-840'},
    {'code': 0xb3ca, 'length': 0x6a, 'hash': 'Skein1024-848'},
    {'code': 0xb3cb, 'length': 0x6b, 'hash': 'Skein1024-856'},
    {'code': 0xb3cc, 'length': 0x6c, 'hash': 'Skein1024-864'},
    {'code': 0xb3cd, 'length': 0x6d, 'hash': 'Skein1024-872'},
    {'code': 0xb3ce, 'length': 0x6e, 'hash': 'Skein1024-880'},
    {'code': 0xb3cf, 'length': 0x6f, 'hash': 'Skein1024-888'},
    {'code': 0xb3d0, 'length': 0x70, 'hash': 'Skein1024-896'},
    {'code': 0xb3d1, 'length': 0x71, 'hash': 'Skein1024-904'},
    {'code': 0xb3d2, 'length': 0x72, 'hash': 'Skein1024-912'},
    {'code': 0xb3d3, 'length': 0x73, 'hash': 'Skein1024-920'},
    {'code': 0xb3d4, 'length': 0x74, 'hash': 'Skein1024-928'},
    {'code': 0xb3d5, 'length': 0x75, 'hash': 'Skein1024-936'},
    {'code': 0xb3d6, 'length': 0x76, 'hash': 'Skein1024-944'},
    {'code': 0xb3d7, 'length': 0x77, 'hash': 'Skein1024-952'},
    {'code': 0xb3d8, 'length': 0x78, 'hash': 'Skein1024-960'},
    {'code': 0xb3d9, 'length': 0x79, 'hash': 'Skein1024-968'},
    {'code': 0xb3da, 'length': 0x7a, 'hash': 'Skein1024-976'},
    {'code': 0xb3db, 'length': 0x7b, 'hash': 'Skein1024-984'},
    {'code': 0xb3dc, 'length': 0x7c, 'hash': 'Skein1024-992'},
    {'code': 0xb3dd, 'length': 0x7d, 'hash': 'Skein1024-1000'},
    {'code': 0xb3de, 'length': 0x7e, 'hash': 'Skein1024-1008'},
    {'code': 0xb3df, 'length': 0x7f, 'hash': 'Skein1024-1016'},
    {'code': 0xb3e0, 'length': 0x80, 'hash': 'Skein1024-1024'},
)

HASH_CODES = {x['hash']: x['code'] for x in HASH_TABLE}
CODE_HASHES = {x['code']: x['hash'] for x in HASH_TABLE}
HASH_LENGTHS = {x['code']: x.get('length') for x in HASH_TABLE}
