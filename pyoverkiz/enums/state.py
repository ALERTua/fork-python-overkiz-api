import sys
from enum import unique

# Since we support Python versions lower than 3.11, we use
# a backport for StrEnum when needed.
if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from backports.strenum import StrEnum


@unique
class OverkizAttribute(StrEnum):
    """Device attributes used by Overkiz."""

    CORE_FIRMWARE_REVISION = "core:FirmwareRevision"
    CORE_MANUFACTURER = "core:Manufacturer"
    CORE_MANUFACTURER_REFERENCE = "core:ManufacturerReference"
    CORE_MAX_SETTABLE_VALUE = "core:MaxSettableValue"
    CORE_MEASURED_VALUE_TYPE = "core:MeasuredValueType"
    CORE_MIN_SETTABLE_VALUE = "core:MinSettableValue"
    CORE_ELECTRIC_POWER_CONSUMPTION_STATE_MEASURED_VALUE_TYPE = (
        "core:ElectricPowerConsumptionStateMeasuredValueType"
    )
    CORE_SUPPORTED_ALIASES = "core:SupportedAliases"
    CORE_SUPPORTED_OPTIONS = "core:SupportedOptions"
    CORE_TECHNOLOGY = "core:Technology"
    HOMEKIT_SETUP_CODE = "homekit:SetupCode"
    OGP_FEATURES = "ogp:Features"


@unique
class OverkizState(StrEnum):
    """Device states used by Overkiz."""

    CORE_ABSENCE_COOLING_TARGET_TEMPERATURE = (
        "core:AbsenceCoolingTargetTemperatureState"
    )
    CORE_ABSENCE_END_DATE_TIME = "core:AbsenceEndDateTimeState"
    CORE_ABSENCE_HEATING_TARGET_TEMPERATURE = (
        "core:AbsenceHeatingTargetTemperatureState"
    )
    CORE_ACTIVE_COOLING_TIME_PROGRAM = "core:ActiveCoolingTimeProgramState"
    CORE_ACTIVE_HEATING_TIME_PROGRAM = "core:ActiveHeatingTimeProgramState"
    CORE_ACTIVE_ZONES = "core:ActiveZonesState"
    CORE_ACTIVATED_OPTIONS = "core:ActivatedOptionsState"
    CORE_ASSEMBLY = "core:AssemblyState"
    CORE_AUTO_MANU_MODE = "core:AutoManuModeState"
    CORE_AVAILABILITY = "core:AvailabilityState"
    CORE_BATTERY = "core:BatteryState"
    CORE_BATTERY_LEVEL = "core:BatteryLevelState"
    CORE_BLUE_COLOR_INTENSITY = "core:BlueColorIntensityState"
    CORE_BOOST_ELECTRIC_POWER_CONSUMPTION = "core:BoostElectricPowerConsumptionState"
    CORE_BOOST_END_DATE = "core:BoostEndDateState"
    CORE_BOOST_MODE_DURATION = "core:BoostModeDurationState"
    CORE_BOOST_ON_OFF = "core:BoostOnOffState"
    CORE_BOOST_START_DATE = "core:BoostStartDateState"
    CORE_BOTTOM_TANK_WATER_TEMPERATURE = "core:BottomTankWaterTemperatureState"
    CORE_CLOSURE = "core:ClosureState"
    CORE_CLOSURE_OR_ROCKER_POSITION = "core:ClosureOrRockerPositionState"
    CORE_CLOUD_DEVICE_STATUS = "core:CloudDeviceStatusState"
    CORE_CO2_CONCENTRATION = "core:CO2ConcentrationState"
    CORE_COMFORT_COOLING_TARGET_TEMPERATURE = (
        "core:ComfortCoolingTargetTemperatureState"
    )
    CORE_COMFORT_HEATING_TARGET_TEMPERATURE = (
        "core:ComfortHeatingTargetTemperatureState"
    )
    CORE_COMFORT_ROOM_TEMPERATURE = "core:ComfortRoomTemperatureState"
    CORE_COMFORT_TARGET_DWH_TEMPERATURE = "core:ComfortTargetDHWTemperatureState"
    CORE_CONSUMPTION_TARIFF1 = "core:ConsumptionTariff1State"
    CORE_CONSUMPTION_TARIFF2 = "core:ConsumptionTariff2State"
    CORE_CONSUMPTION_TARIFF3 = "core:ConsumptionTariff3State"
    CORE_CONSUMPTION_TARIFF4 = "core:ConsumptionTariff4State"
    CORE_CONSUMPTION_TARIFF5 = "core:ConsumptionTariff5State"
    CORE_CONSUMPTION_TARIFF6 = "core:ConsumptionTariff6State"
    CORE_CONSUMPTION_TARIFF7 = "core:ConsumptionTariff7State"
    CORE_CONSUMPTION_TARIFF8 = "core:ConsumptionTariff8State"
    CORE_CONSUMPTION_TARIFF9 = "core:ConsumptionTariff9State"
    CORE_CONTACT = "core:ContactState"
    CORE_CONTROL_WATER_TARGET_TEMPERATURE = "core:ControlWaterTargetTemperatureState"
    CORE_CO_CONCENTRATION = "core:COConcentrationState"
    CORE_COOLING_ON_OFF = "core:CoolingOnOffState"
    CORE_COOLING_TARGET_TEMPERATURE = "core:CoolingTargetTemperatureState"
    CORE_DATETIME = "core:DateTimeState"
    CORE_DEPLOYMENT = "core:DeploymentState"
    CORE_DEROGATED_TARGET_TEMPERATURE = "core:DerogatedTargetTemperatureState"
    CORE_DEROGATION_ACTIVATION = "core:DerogationActivationState"
    CORE_DEROGATION_ON_OFF = "core:DerogationOnOffState"
    CORE_DEVICE_SERIAL_NUMBER = "core:DeviceSerialNumberState"
    CORE_DHW_DEROGATION_AVAILABILITY = "core:DHWDerogationAvailabilityState"
    CORE_DHW_TEMPERATURE = "core:DHWTemperatureState"
    CORE_DISCRETE_RSSI_LEVEL = "core:DiscreteRSSILevelState"
    CORE_DWH_ON_OFF = "core:DHWOnOffState"
    CORE_ECO_COOLING_TARGET_TEMPERATURE = "core:EcoCoolingTargetTemperatureState"
    CORE_ECO_HEATING_TARGET_TEMPERATURE = "core:EcoHeatingTargetTemperatureState"
    CORE_ECO_ROOM_TEMPERATURE = "core:EcoRoomTemperatureState"
    CORE_ECO_TARGET_DWH_TEMPERATURE = "core:EcoTargetDHWTemperatureState"
    CORE_ELECTRIC_ENERGY_CONSUMPTION = "core:ElectricEnergyConsumptionState"
    CORE_ELECTRIC_POWER_CONSUMPTION = "core:ElectricPowerConsumptionState"
    CORE_EXPECTED_NUMBER_OF_SHOWER = "core:ExpectedNumberOfShowerState"
    CORE_FIRMWARE_REVISION = "core:FirmwareRevision"
    CORE_FOSSIL_ENERGY_CONSUMPTION = "core:FossilEnergyConsumptionState"
    CORE_GAS_CONSUMPTION = "core:GasConsumptionState"
    CORE_GAS_DETECTION = "core:GasDetectionState"
    CORE_GREEN_COLOR_INTENSITY = "core:GreenColorIntensityState"
    CORE_HOLIDAYS_MODE = "core:HolidaysModeState"
    CORE_HEATING_COOLING_AUTO_SWITCH = "core:HeatingCoolingAutoSwitchState"
    CORE_HEATING_DEROGATION_AVAILABILITY = "core:HeatingDerogationAvailabilityState"
    CORE_HEATING_ON_OFF = "core:HeatingOnOffState"
    CORE_HEATING_STATUS = "core:HeatingStatusState"
    CORE_HEATING_TARGET_TEMPERATURE = "core:HeatingTargetTemperatureState"
    CORE_INTRUSION = "core:IntrusionState"
    CORE_LEVEL = "core:LevelState"
    CORE_LIGHT_INTENSITY = "core:LightIntensityState"
    CORE_LOCKED_UNLOCKED = "core:LockedUnlockedState"
    CORE_LUMINANCE = "core:LuminanceState"
    CORE_MANUFACTURER_NAME = "core:ManufacturerNameState"
    CORE_MIN_SETPOINT = "core:MinSetpointState"
    CORE_MAX_SETPOINT = "core:MaxSetpointState"
    CORE_MAXIMAL_SHOWER_MANUAL_MODE = "core:MaximalShowerManualModeState"
    CORE_MAXIMAL_TEMPERATURE_MANUAL_MODE = "core:MaximalTemperatureManualModeState"
    CORE_MAXIMUM_COOLING_TARGET_TEMPERATURE = (
        "core:MaximumCoolingTargetTemperatureState"
    )
    CORE_MAXIMUM_HEATING_TARGET_TEMPERATURE = (
        "core:MaximumHeatingTargetTemperatureState"
    )
    CORE_MAXIMUM_TEMPERATURE = "core:MaximumTemperatureState"
    CORE_MEMORIZED_1_POSITION = "core:Memorized1PositionState"
    CORE_MIDDLE_WATER_TEMPERATURE_IN = "core:MiddleWaterTemperatureInState"
    CORE_MINIMAL_SHOWER_MANUAL_MODE = "core:MinimalShowerManualModeState"
    CORE_MINIMAL_TEMPERATURE_MANUAL_MODE = "core:MinimalTemperatureManualModeState"
    CORE_MINIMUM_COOLING_TARGET_TEMPERATURE = (
        "core:MinimumCoolingTargetTemperatureState"
    )
    CORE_MINIMUM_HEATING_TARGET_TEMPERATURE = (
        "core:MinimumHeatingTargetTemperatureState"
    )
    CORE_MINIMUM_TEMPERATURE = "core:MinimumTemperatureState"
    CORE_MODEL = "core:ModelState"
    CORE_MOVING = "core:MovingState"
    CORE_NAME = "core:NameState"
    CORE_NUMBER_OF_SHOWER_REMAINING = "core:NumberOfShowerRemainingState"
    CORE_NUMBER_OF_TANK = "core:NumberOfTankState"
    CORE_OCCUPANCY = "core:OccupancyState"
    CORE_ON_OFF = "core:OnOffState"
    CORE_OPEN_CLOSED = "core:OpenClosedState"
    CORE_OPEN_CLOSED_PARTIAL = "core:OpenClosedPartialState"
    CORE_OPEN_CLOSED_PEDESTRIAN = "core:OpenClosedPedestrianState"
    CORE_OPEN_CLOSED_UNKNOWN = "core:OpenClosedUnknownState"
    CORE_OPEN_CLOSED_VALVE = "core:OpenClosedValveState"
    CORE_OPEN_WINDOW_DETECTION_ACTIVATION = "core:OpenWindowDetectionActivationState"
    CORE_OPERATING_MODE = "core:OperatingModeState"
    CORE_PEDESTRIAN_POSITION = "core:PedestrianPositionState"
    CORE_POWER_HEAT_ELECTRICAL_IN = "core:PowerHeatElectricalInState"
    CORE_POWER_SUPPLY_UP_DOWN = "core:PowerSupplyUpDownState"
    CORE_PRIORITY_LOCK_TIMER = "core:PriorityLockTimerState"
    CORE_PRODUCT_MODEL_NAME = "core:ProductModelNameState"
    CORE_PROGRAMMING_AVAILABLE = "core:ProgrammingAvailableState"
    CORE_RAIN = "core:RainState"
    CORE_RED_COLOR_INTENSITY = "core:RedColorIntensityState"
    CORE_RELATIVE_HUMIDITY = "core:RelativeHumidityState"
    CORE_REMAINING_HOT_WATER = "core:RemainingHotWaterState"
    CORE_RSSI_LEVEL = "core:RSSILevelState"
    CORE_SECURED_POSITION_TEMPERATURE = "core:SecuredPositionTemperatureState"
    CORE_SENSOR_DEFECT = "core:SensorDefectState"
    CORE_SLATE_ORIENTATION = "core:SlateOrientationState"
    CORE_SLATS_OPEN_CLOSED = "core:SlatsOpenClosedState"
    CORE_SLATS_ORIENTATION = "core:SlatsOrientationState"
    CORE_SMOKE = "core:SmokeState"
    CORE_STATUS = "core:StatusState"
    CORE_STOP_RELAUNCH = "core:StopRelaunchState"
    CORE_SUN_ENERGY = "core:SunEnergyState"
    CORE_TARGET_CLOSURE = "core:TargetClosureState"
    CORE_TARGET_DWH_TEMPERATURE = "core:TargetDHWTemperatureState"
    CORE_TARGET_TEMPERATURE = "core:TargetTemperatureState"
    CORE_TEMPERATURE = "core:TemperatureState"
    CORE_THERMAL_CONFIGURATION = "core:ThermalConfigurationState"
    CORE_THERMAL_ENERGY_CONSUMPTION = "core:ThermalEnergyConsumptionState"
    CORE_THREE_WAY_HANDLE_DIRECTION = "core:ThreeWayHandleDirectionState"
    CORE_TIME_PROGRAM_1 = "core:TimeProgram1State"
    CORE_TIME_PROGRAM_2 = "core:TimeProgram2State"
    CORE_TIME_PROGRAM_3 = "core:TimeProgram3State"
    CORE_TIME_PROGRAM_4 = "core:TimeProgram4State"
    CORE_V40_WATER_VOLUME_ESTIMATION = "core:V40WaterVolumeEstimationState"
    CORE_VIBRATION = "core:VibrationState"
    CORE_WATER_CONSUMPTION = "core:WaterConsumptionState"
    CORE_WATER_DETECTION = "core:WaterDetectionState"
    CORE_WATER_TARGET_TEMPERATURE = "core:WaterTargetTemperatureState"
    CORE_WEATHER_STATUS = "core:WeatherStatusState"
    CORE_WIND_SPEED = "core:WindSpeedState"
    CORE_ZONE_NUMBER = "core:ZonesNumberState"
    HLRRWIFI_FAN_SPEED = "hlrrwifi:FanSpeedState"
    HLRRWIFI_LEAVE_HOME = "hlrrwifi:LeaveHomeState"
    HLRRWIFI_MAIN_OPERATION = "hlrrwifi:MainOperationState"
    HLRRWIFI_MODE_CHANGE = "hlrrwifi:ModeChangeState"
    HLRRWIFI_OUTDOOR_TEMPERATURE = "hlrrwifi:OutdoorTemperatureState"
    HLRRWIFI_ROOM_TEMPERATURE = "hlrrwifi:RoomTemperatureState"
    HLRRWIFI_SWING = "hlrrwifi:SwingState"
    INTERNAL_CURRENT_ALARM_MODE = "internal:CurrentAlarmModeState"
    INTERNAL_INTRUSION_DETECTED = "internal:IntrusionDetectedState"
    INTERNAL_TARGET_ALARM_MODE = "internal:TargetAlarmModeState"
    IO_ABSENCE_SCHEDULING_AVAILABILITY = "io:AbsenceSchedulingAvailabilityState"
    IO_ABSENCE_SCHEDULING_MODE = "io:AbsenceSchedulingModeState"
    IO_AIR_DEMAND_MODE = "io:AirDemandModeState"
    IO_AWAY_MODE_DURATION = "io:AwayModeDurationState"
    IO_BYPASS_ACTIVATION = "io:ByPassActivationState"
    IO_DEROGATION_HEATING_MODE = "io:DerogationHeatingModeState"
    IO_DEROGATION_REMAINING_TIME = "io:DerogationRemainingTimeState"
    IO_DHW_ABSENCE_MODE = "io:DHWAbsenceModeState"
    IO_DHW_BOOST_MODE = "io:DHWBoostModeState"
    IO_DHW_MODE = "io:DHWModeState"
    IO_EFFECTIVE_TEMPERATURE_SETPOINT = "io:EffectiveTemperatureSetpointState"
    IO_ELECTRIC_BOOSTER_OPERATING_TIME = "io:ElectricBoosterOperatingTimeState"
    IO_FORCE_HEATING = "io:ForceHeatingState"
    IO_HEAT_PUMP_OPERATING_TIME = "io:HeatPumpOperatingTimeState"
    IO_INLET_ENGINE = "io:InletEngineState"
    IO_LAST_PASS_APC_OPERATING_MODE = "io:LastPassAPCOperatingModeState"
    IO_LOCK_KEY_ACTIVATION = "io:LockKeyActivationState"
    IO_MEMORIZED_SIMPLE_VOLUME = "io:MemorizedSimpleVolumeState"
    IO_MIDDLE_WATER_TEMPERATURE = "io:MiddleWaterTemperatureState"
    IO_MODEL = "io:ModelState"
    IO_OPERATING_MODE_CAPABILITIES = "io:OperatingModeCapabilitiesState"
    IO_OUTLET_ENGINE = "io:OutletEngineState"
    IO_PASS_APCDHW_CONFIGURATION = "io:PassAPCDHWConfigurationState"
    IO_PASS_APCDHW_PROFILE = "io:PassAPCDHWProfileState"
    IO_PASS_APCDWH_MODE = "io:PassAPCDHWModeState"
    IO_PASS_APC_COOLING_MODE = "io:PassAPCCoolingModeState"
    IO_PASS_APC_COOLING_PROFILE = "io:PassAPCCoolingProfileState"
    IO_PASS_APC_HEATING_MODE = "io:PassAPCHeatingModeState"
    IO_PASS_APC_HEATING_PROFILE = "io:PassAPCHeatingProfileState"
    IO_PASS_APC_OPERATING_MODE = "io:PassAPCOperatingModeState"
    IO_PASS_APC_PRODUCT_TYPE = "io:PassAPCProductTypeState"
    IO_POWER_HEAT_ELECTRICAL = "io:PowerHeatElectricalState"
    IO_POWER_HEAT_PUMP = "io:PowerHeatPumpState"
    IO_PRIORITY_LOCK_LEVEL = "io:PriorityLockLevelState"
    IO_PRIORITY_LOCK_ORIGINATOR = "io:PriorityLockOriginatorState"
    IO_SENSOR_ROOM = "io:SensorRoomState"
    IO_TARGET_HEATING_LEVEL = "io:TargetHeatingLevelState"
    IO_THERMAL_SCHEDULING_AVAILABILITY = "io:ThermalSchedulingAvailabilityState"
    IO_THERMAL_SCHEDULING_MODE = "io:ThermalSchedulingModeState"
    IO_TOWEL_DRYER_TEMPORARY_STATE = "io:TowelDryerTemporaryStateState"
    IO_VALVE_INSTALLATION_MODE = "io:ValveInstallationModeState"
    IO_VENTILATION_CONFIGURATION_MODE = "io:VentilationConfigurationModeState"
    IO_VENTILATION_MODE = "io:VentilationModeState"
    IO_VIBRATION_DETECTED = "io:VibrationDetectedState"
    MODBUSLINK_ANTI_LEGIONELLOSIS = "modbuslink:AntiLegionellosisState"
    MODBUSLINK_DHW_ABSENCE_MODE = "modbuslink:DHWAbsenceModeState"
    MODBUSLINK_DHW_BOOST_MODE = "modbuslink:DHWBoostModeState"
    MODBUSLINK_DHW_CAPACITY = "modbuslink:DHWCapacityState"
    MODBUSLINK_DHW_ERROR = "modbuslink:DHWErrorState"
    MODBUSLINK_DHW_MODE = "modbuslink:DHWModeState"
    MODBUSLINK_ELECTRIC_BOOSTER_OPERATING_TIME = (
        "modbuslink:ElectricBoosterOperatingTimeState"
    )
    MODBUSLINK_HEAT_PUMP_OPERATING_TIME = "modbuslink:HeatPumpOperatingTimeState"
    MODBUSLINK_IHM_TYPE = "modbuslink:IHMTypeState"
    MODBUSLINK_MANUFACTURER = "modbuslink:ManufacturerState"
    MODBUSLINK_MIDDLE_WATER_TEMPERATURE = "modbuslink:MiddleWaterTemperatureState"
    MODBUSLINK_NUMBER_CONTROL_SHOWER_REQUEST = (
        "modbuslink:NumberControlShowerRequestState"
    )
    MODBUSLINK_OPERATING_RANGE = "modbuslink:OperatingRangeState"
    MODBUSLINK_POWER_HEAT_ELECTRICAL = "modbuslink:PowerHeatElectricalState"
    MODBUSLINK_POWER_HEAT_PUMP = "modbuslink:PowerHeatPumpState"
    MODBUSLINK_PROGRAMMING_SLOTS = "modbuslink:ProgrammingSlotsState"
    MODBUSLINK_SMART_GRID_OPTION = "modbuslink:SmartGridOptionState"
    MODBUS_ALARM_NUMBER = "modbus:AlarmNumberState"
    MODBUS_AUTO_MANU_MODE_ZONE_1 = "modbus:AutoManuModeZone1State"
    MODBUS_CAUSE_OF_STOPPAGE = "modbus:CauseOfStoppageState"
    MODBUS_CENTRAL_SETTING_1 = "modbus:CentralSetting1State"
    MODBUS_CENTRAL_SETTING_2 = "modbus:CentralSetting2State"
    MODBUS_CENTRAL_SETTING_3 = "modbus:CentralSetting3State"
    MODBUS_COMPRESSOR_CURRENT_VALUE = "modbus:CompressorCurrentValueState"
    MODBUS_COMPRESSOR_FREQUENCY = "modbus:CompressorFrequencyState"
    MODBUS_COMPRESSOR_RUNNING_CURRENT = "modbus:CompressorRunningCurrentState"
    MODBUS_CONTROL_BLOCK_MENU = "modbus:ControlBlockMenuState"
    MODBUS_CONTROL_COMMUNICATION_ALARM_BIT = "modbus:ControlCommunicationAlarmBitState"
    MODBUS_CONTROL_DHW = "modbus:ControlDHWState"
    MODBUS_CONTROL_DHW_SETTING_TEMPERATURE = "modbus:ControlDHWSettingTemperatureState"
    MODBUS_CONTROL_UNIT = "modbus:ControlUnitState"
    MODBUS_CONTROL_UNIT_MODE = "modbus:ControlUnitModeState"
    MODBUS_DEFROSTING = "modbus:DefrostingState"
    MODBUS_DHW_MODE = "modbus:DHWModeState"
    MODBUS_DISCHARGE_GAS_TEMPERATURE = "modbus:DischargeGasTemperatureState"
    MODBUS_DISCHARGE_PRESSURE = "modbus:DischargePressureState"
    MODBUS_DISCHARGE_TEMPERATURE = "modbus:DischargeTemperatureState"
    MODBUS_ECO_MODE_OFFSET = "modbus:EcoModeOffsetState"
    MODBUS_ECO_MODE_OFFSET_TARGET = "modbus:EcoModeOffsetTargetState"
    MODBUS_EVAPORATING_TEMPERATURE = "modbus:EvaporatingTemperatureState"
    MODBUS_EVAPORATION_TEMPERATURE = "modbus:EvaporationTemperatureState"
    MODBUS_GAS_TEMPERATURE = "modbus:GasTemperatureState"
    MODBUS_HARDWARE_VERSION = "modbus:HardwareVersionState"
    MODBUS_HLINK_COMMUNICATION_ALARM = "modbus:HLinkCommunicationAlarmState"
    MODBUS_INDOOR_EXPANSION_VALVE = "modbus:IndoorExpansionValveState"
    MODBUS_INDOOR_EXPANSION_VALVE_OPENING = "modbus:IndoorExpansionValveOpeningState"
    MODBUS_INVERTER_OPERATION_FREQUENCY = "modbus:InverterOperationFrequencyState"
    MODBUS_LCD_CENTRAL_MODE = "modbus:LCDCentralModeState"
    MODBUS_LCD_SOFTWARE_NUMBER = "modbus:LCDSoftwareNumberState"
    MODBUS_LIQUID_TEMPERATURE = "modbus:LiquidTemperatureState"
    MODBUS_LIQUID_TEMPERATURE_THMI = "modbus:LiquidTemperatureTHMIState"
    MODBUS_MIXING_VALVE_POSITION = "modbus:MixingValvePositionState"
    MODBUS_OPERATION = "modbus:OperationState"
    MODBUS_OUTDOOR_AMBIENT_TEMPERATURE = "modbus:OutdoorAmbientTemperatureState"
    MODBUS_OUTDOOR_EXPANSION_VALVE = "modbus:OutdoorExpansionValveState"
    MODBUS_OUTDOOR_UNIT_AMBIENT = "modbus:OutdoorUnitAmbientState"
    MODBUS_PCB1_SOFTWARE_NUMBER = "modbus:PCB1SoftwareNumberState"
    MODBUS_PRODUCT_SPEC_CODE = "modbus:ProductSpecCodeState"
    MODBUS_RETRY_CODE = "modbus:RetryCodeState"
    MODBUS_ROOM_AMBIENT_TEMPERATURE_STATUS_ZONE_1 = (
        "modbus:RoomAmbientTemperatureStatusZone1State"
    )
    MODBUS_ROOM_THERMOSTAT_SET_TEMPERATURE_C1 = (
        "modbus:RoomThermostatSetTemperatureC1State"
    )
    MODBUS_ROOM_THERMOSTAT_SET_TEMPERATURE_C2 = (
        "modbus:RoomThermostatSetTemperatureC2State"
    )
    MODBUS_ROOM_THERMOSTAT_TEMPERATURE_C1 = "modbus:RoomThermostatTemperatureC1State"
    MODBUS_ROOM_THERMOSTAT_TEMPERATURE_C2 = "modbus:RoomThermostatTemperatureC2State"
    MODBUS_SECOND_AMBIENT_AVERAGE_TEMPERATURE = (
        "modbus:SecondAmbientAverageTemperatureState"
    )
    MODBUS_SECOND_AMBIENT_TEMPERATURE = "modbus:SecondAmbientTemperatureState"
    MODBUS_SOFTWARE_NUMBER = "modbus:SoftwareNumberState"
    MODBUS_SOFTWARE_VERSION = "modbus:SoftwareVersionState"
    MODBUS_SPACE_MODE = "modbus:SpaceModeState"
    MODBUS_STATUS_BLOCK_MENU = "modbus:StatusBlockMenuState"
    MODBUS_STATUS_COMMUNICATION_ALARM_BIT = "modbus:StatusCommunicationAlarmBitState"
    MODBUS_STATUS_UNIT_MODE = "modbus:StatusUnitModeState"
    MODBUS_SUCTION_PRESSURE = "modbus:SuctionPressureState"
    MODBUS_SUCTION_TEMPERATURE = "modbus:SuctionTemperatureState"
    MODBUS_SYSTEM_CONFIGURATION = "modbus:SystemConfigurationState"
    MODBUS_SYSTEM_STATUS_2 = "modbus:SystemStatus2State"
    MODBUS_TAHOMA_ROOM_THERMOSTAT_AVAILABLE = (
        "modbus:TahomaRoomThermostatAvailableState"
    )
    MODBUS_THERMOSTAT_SETTING_CONTROL_ZONE_1 = (
        "modbus:ThermostatSettingControlZone1State"
    )
    MODBUS_THERMOSTAT_SETTING_STATUS_ZONE_1 = "modbus:ThermostatSettingStatusZone1State"
    MODBUS_UNIT_MODEL = "modbus:UnitModelState"
    MODBUS_VIRTUAL_ECO_COMFORT_MODE = "modbus:VirtualEcoComfortModeState"
    MODBUS_WATER_FLOW_LEVEL = "modbus:WaterFlowLevelState"
    MODBUS_WATER_INLET_UNIT_TEMPERATURE = "modbus:WaterInletUnitTemperatureState"
    MODBUS_WATER_OUTLET_HP_TEMPERATURE = "modbus:WaterOutletHpTemperatureState"
    MODBUS_WATER_OUTLET_TEMPERATURE_2 = "modbus:WaterOutletTemperature2State"
    MODBUS_WATER_OUTLET_TEMPERATURE_3 = "modbus:WaterOutletTemperature3State"
    MODBUS_WATER_OUTLET_UNIT_TEMPERATURE = "modbus:WaterOutletUnitTemperatureState"
    MODBUS_WATER_PUMP_SPEED = "modbus:WaterPumpSpeedState"
    MODBUS_WATER_TEMPERATURE_SETTING = "modbus:WaterTemperatureSettingState"
    MODBUS_YUTAKI_TARGET_MODE = "modbus:YutakiTargetModeState"
    MODBUS_YUTAKI_VIRTUAL_OPERATING_MODE = "modbus:YutakiVirtualOperatingModeState"

    MYFOX_ALARM_STATUS = "myfox:AlarmStatusState"
    MYFOX_ALERT_TRESPASS = "myfox:AlertTrespassState"
    MYFOX_SHUTTER_STATUS = "myfox:ShutterStatusState"
    OVP_FAN_SPEED = "ovp:FanSpeedState"
    OVP_HEATING_TEMPERATURE_INTERFACE_ACTIVE_MODE = (
        "ovp:HeatingTemperatureInterfaceActiveModeState"
    )
    OVP_HEATING_TEMPERATURE_INTERFACE_OPERATING_MODE = (
        "ovp:HeatingTemperatureInterfaceOperatingModeState"
    )
    OVP_HEATING_TEMPERATURE_INTERFACE_SETPOINT_MODE = (
        "ovp:HeatingTemperatureInterfaceSetPointModeState"
    )
    OVP_LEAVE_HOME = "ovp:LeaveHomeState"
    OVP_MAIN_OPERATION = "ovp:MainOperationState"
    OVP_MODE_CHANGE = "ovp:ModeChangeState"
    OVP_OUTDOOR_TEMPERATURE = "ovp:OutdoorTemperatureState"
    OVP_ROOM_TEMPERATURE = "ovp:RoomTemperatureState"
    OVP_SWING = "ovp:SwingState"
    OVP_TEMPERATURE_CHANGE = "ovp:TemperatureChangeState"
    RAMSES_RAMSES_OPERATING_MODE = "ramses:RAMSESOperatingModeState"
    RTDS_CONTROLLER_BATTERY = "rtds:ControllerBatteryState"
    RTDS_CONTROLLER_BIP = "rtds:ControllerBipState"
    RTDS_CONTROLLER_ORDER_TYPE = "rtds:ControllerOrderTypeState"
    RTDS_CONTROLLER_ORIGINATOR = "rtds:ControllerOriginatorState"
    RTDS_CONTROLLER_SENSING = "rtds:ControllerSensingState"
    RTDS_CONTROLLER_SIREN = "rtds:ControllerSirenState"
    SOMFY_THERMOSTAT_AT_HOME_TARGET_TEMPERATURE = (
        "somfythermostat:AtHomeTargetTemperatureState"
    )
    SOMFY_THERMOSTAT_AWAY_MODE_TARGET_TEMPERATURE = (
        "somfythermostat:AwayModeTargetTemperatureState"
    )
    SOMFY_THERMOSTAT_DEROGATION_HEATING_MODE = (
        "somfythermostat:DerogationHeatingModeState"
    )
    SOMFY_THERMOSTAT_FREEZE_MODE_TARGET_TEMPERATURE = (
        "somfythermostat:FreezeModeTargetTemperatureState"
    )
    SOMFY_THERMOSTAT_HEATING_MODE = "somfythermostat:HeatingModeState"
    SOMFY_THERMOSTAT_SLEEPING_MODE_TARGET_TEMPERATURE = (
        "somfythermostat:SleepingModeTargetTemperatureState"
    )
    VERISURE_ALARM_PANEL_MAIN_ARM_TYPE = "verisure:AlarmPanelMainArmTypeState"
