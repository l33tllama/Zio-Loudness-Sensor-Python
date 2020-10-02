import smbus2

class LoudnessSensor():
    I2C_ADDR = 0x38
    CMD_GET_VALUE = 0x05
    CMD_LED_ON = 0x01
    CMD_LED_OFF = 0x00
    DEVICE_REG_MODE1 = 0x00
    bus = {}

    def __init__(self):
        self.bus = smbus2.SMBus(1)

    def led_on(self):
        self.bus.write_byte(self.I2C_ADDR, self.CMD_LED_ON)

    def led_off(self):
        self.bus.write_byte(self.I2C_ADDR, self.CMD_LED_OFF)

    def get_value(self):
        self.bus.write_byte(self.I2C_ADDR, self.CMD_GET_VALUE)
        data = self.bus.read_i2c_block_data(self.I2C_ADDR, self.CMD_GET_VALUE, 2)
        adc_value_l = data[0]
        adc_value_h = data[1]
        adc_value = adc_value_h << 8
        adc_value |= adc_value_l
        return adc_value
