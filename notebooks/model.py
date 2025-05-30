# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2025-02-14T18:59:58+00:00

from __future__ import annotations

from datetime import date, time
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class AddressDataSimple(BaseModel):
    city: Optional[str] = Field(None, description='City, district, suburb, town, or village.', title='City')
    postal_code: Optional[str] = Field(
        None,
        description='ZIP or postal code. If french postal code, it should be a pure number, without letters.',
        title='Postal Code',
    )
    country: Optional[str] = Field(
        None,
        description='Two-letter country code (ISO 3166-1 alpha-2).',
        title='Country',
    )
    line1: Optional[str] = Field(
        None,
        description='Address line 1 (e.g., street, PO Box, or company name).',
        title='Line1',
    )
    line2: Optional[str] = Field(
        None,
        description='Address line 2 (e.g., apartment, suite, unit, or building).',
        title='Line2',
    )


class ClientData(BaseModel):
    company_name: Optional[str] = Field(None, description='Legal company name for billing', title='Company Name')
    SIREN: Optional[str] = Field(
        None,
        description='SIREN number for billing and tax purposes. Usually located at the top or the very bottom of the document. (small text), and located alongside the other billing informations',
        title='Siren',
    )
    VAT_number_thinking: Optional[str] = Field(
        None,
        description='The VAT number is present for billing and tax purposes. Usually located at the top or the very bottom of the document, and located alongside the other billing informations (small text).\nIn France the VAT number format is FR {2 digits validation key} {first 9 digits SIREN number} so try use the SIREN number if available to help validate the VAT number.\nDocument your reasoning for the VAT number identification:\n1. Look for numbers prefixed with \'FR\' or labeled as \'TVA\', \'VAT\', or \'n° TVA\'\n2. Verify the format matches FR followed by key of 2 digits and 9 digits of SIREN number\n3. Note where you found it in the document\n\nExample: "Found VAT number FR12345678901 in footer next to SIREN number"\n\nIf multiple possible VAT numbers exist, explain your choice. If none found, state "No VAT number identified in document.',
        title='Vat Number Thinking',
    )
    VAT_number: Optional[str] = Field(None, description='VAT number Value', title='Vat Number')
    city: Optional[str] = Field(
        None,
        description='City, district, suburb, town, or village of billing address',
        title='City',
    )
    postal_code: Optional[str] = Field(
        None,
        description='ZIP or postal code of billing address. If french postal code, it should be a pure number, without letters.',
        title='Postal Code',
    )
    country: Optional[str] = Field(
        None,
        description='Two-letter country code (ISO 3166-1 alpha-2).',
        title='Country',
    )
    code: Optional[str] = Field(
        None,
        description='Unique code for the client used to connect the booking to the client in the TMS. It is rarely provided. If not provided, set to None',
        title='Code',
    )
    email: Optional[str] = Field(None, description='Client email address', title='Email')


class UNPackingGroup(Enum):
    I = 'I'
    II = 'II'
    III = 'III'


class ADRTunnelCode(Enum):
    B = 'B'
    B1000C = 'B1000C'
    B_D = 'B/D'
    B_E = 'B/E'
    C = 'C'
    C5000D = 'C5000D'
    C_D = 'C/D'
    C_E = 'C/E'
    D = 'D'
    D_E = 'D/E'
    E = 'E'
    field_ = '-'


class DangerousGoodsInfoData(BaseModel):
    thinking: Optional[str] = Field(
        None,
        description='Document your analysis of the goods information from the source document. Include:\n\n1. Description of what\'s being transported\n2. Any reference numbers or codes found\n3. Special handling requirements\n4. Equipment needs\n5. Safety considerations\n6. Documentation requirements\n7. The presence of returnable Euro pallets (it has to be explicitly stated that the pallets are EU pallets in the source document in the sender section (not in the legal mentions))\n\n*Some observations you may consider about the weight:*\n- Sometimes the weight appears in tons, or kilograms. If the unit is not specified, assume it is in kilograms. However, the weight may appear like "12T400" which means 12.4 tons.\n- Some weight examples: "1500" -> 1500 kg, "1T500" -> 1.500 tons -> 1500 kg, "7T565" -> 7.565 tons -> 7565 kg, "12 tons" -> 12000 kg, "14 tonnes" -> 14000 kg\n\n*Example of thinking output:*\n```\nSource indicates: \n- 12 pallets of automotive parts\n- Reference: ORDER123, BATCH456\n- Requires forklift for unloading\n- Non-stackable items\n- Fragile goods warning labels needed"\n- Weight is in displayed in tons - its value is 5.4 tons, which is equivalent to 5400 kg.\n```\nList all relevant details found in the source document. Do not make assumptions about information that isn\'t explicitly stated.',
        title='Thinking',
    )
    weight: Optional[float] = Field(None, description='Weight of the dangerous good (in kilograms)', title='Weight')
    UN_code: Optional[int] = Field(None, description='UN code of the dangerous good', title='Un Code')
    UN_label: Optional[str] = Field(None, description='UN label of the dangerous good', title='Un Label')
    UN_class: Optional[str] = Field(None, description='UN class of the dangerous good', title='Un Class')
    UN_packing_group: Optional[UNPackingGroup] = Field(
        None,
        description='UN packing group of the dangerous good',
        title='Un Packing Group',
    )
    ADR_tunnel_code: Optional[ADRTunnelCode] = Field(
        None,
        description='ADR tunnel code of the dangerous good',
        title='Adr Tunnel Code',
    )


class DeliveryDatetimeData(BaseModel):
    date: Optional[date] = Field(
        None,
        description='Date of the delivery. ISO 8601 Date Format: YYYY-MM-DD',
        title='Date',
    )
    start_time: Optional[time] = Field(
        None,
        description='Start time of the delivery. ISO 8601 Time Format: hh:mm',
        title='Start Time',
    )
    end_time: Optional[time] = Field(
        None,
        description='End time of the delivery. ISO 8601 Time Format: hh:mm. Must be greater than or equal to the start_time.',
        title='End Time',
    )


class DimensionsData(BaseModel):
    loading_meters_thinking: Optional[str] = Field(
        None,
        description='A loading meter (LM) is a measurement of the cargo space occupied in a truck, calculated based on the item’s footprint relative to the truck’s standard internal width of 2.4 meters. This measurement helps determine how much linear floor space is needed to transport the goods efficiently.\n\nIf loading meters are provided in the source (often labeled as Mètre linéaire (ML) or Mètre plancher (MPL)), use that value directly, noting it as “Using provided value of X loading meters.”\n\nIf not, calculate as follows:\n\n\t1.\tFor each item: (length × width) / 2.4.\n\t2.\tSum all calculated loading meters.\n\nFor example:\n\n\t•\tItem 1 is 3m × 1.2m, so it takes (3 × 1.2) / 2.4 = 1.5 loading meters.\n\t•\tItem 2 is 2m × 1.6m, so it takes (2 × 1.6) / 2.4 = 1.33 loading meters.\n\nTotal loading meters: 1.5 + 1.33 = 2.83 meters\n\nFor each item, write down the formula, insert values, and compute explicitly.\nTake your time to think rigourously. Do not hesitate to write down intermediate steps. WARNING: VOLUME WILL NOT BE IN ml, this is the unit used for loading meters - ml stands for metres lineaires.',
        title='Loading Meters Thinking',
    )
    loading_meters: Optional[float] = Field(None, description='Loading meters value', title='Loading Meters')
    volume_thinking: Optional[str] = Field(
        None,
        description='Volume represents the total space occupied by an item in cubic meters, calculated as (length × width × height).\n\nIf volume is provided in the source, use that value directly and note it as, “Using provided value of X cubic meters.”\n\nIf not, calculate as follows:\n\n\t1.\tFor each item: length × width × height.\n\t2.\tSum the volumes of all items for the total volume.\n\nExample:\n\n\t•\tItem 1: 2m × 1m × 1.5m = 3 cubic meters\n\t•\tItem 2: 1.5m × 1m × 1m = 1.5 cubic meters\n\nTotal volume: 3 + 1.5 = 4.5 cubic meters\n\nFor each item, write down the formula, insert values, and compute explicitly. Take your time to ensure accuracy, and write intermediate steps if necessary.',
        title='Volume Thinking',
    )
    volume: Optional[float] = Field(None, description='Volume value in cubic meters', title='Volume')


class PackingType(Enum):
    pallet = 'pallet'
    bulk = 'bulk'
    container = 'container'
    other = 'other'


class PackingData(BaseModel):
    units: Optional[int] = Field(None, description='Number of units', title='Units')
    packing_type: Optional[PackingType] = Field(
        None,
        description="Type of packing - make sure you don't say it's a pallet (e.g. it says PAL) if you are not sure",
        title='Packing Type',
    )
    supplementary_parcels: Optional[int] = Field(None, description='Number of additional parcels', title='Supplementary Parcels')
    pallets_on_ground_thinking: Optional[str] = Field(
        None,
        description='This field calculates the equivalent floor area occupied by packing units, expressed in terms of standard EUR pallets (1.2m × 0.8m). Follow these steps for each pallet, then sum the results to get the total floor pallet equivalent:\n\n\t1.\tFor each pallet: (length × width) / (1.2 × 0.8).\n\t2.\tSum the calculations to get the total floor pallet equivalent area.\n\nExample Calculations:\n\nExample 1: 6 EUR Pallets (Standard Size)\n\nIf all 6 pallets are standard EUR pallets:\n\n\t•\tEach pallet occupies: (1.2 × 0.8) / (1.2 × 0.8) = 1 pallet equivalent.\n\t•\tTotal for 6 pallets: 1 + 1 + 1 + 1 + 1 + 1 = 6.\n\nSo, floor pallet equivalent = 6.\n\nExample 2: Two Custom Pallets\n\n\t•\tPallet 1: 1.5m × 0.9m, so 1.5 × 0.9 / (1.2 × 0.8) ≈ 1.41.\n\t•\tPallet 2: 1.0m × 1.1m, so 1.0 × 1.1 / (1.2 × 0.8) ≈ 1.15.\n\nTotal floor pallet equivalent = 1.41 + 1.15 = 2.56.\n\nFor each pallet, write down the formula, insert values, and compute explicitly.\nTake your time to think rigourously. Do not hesitate to write down intermediate steps.',
        title='Pallets On Ground Thinking',
    )
    pallets_on_ground: Optional[float] = Field(None, description='pallets on ground value', title='Pallets On Ground')
    number_eur_pallet: Optional[int] = Field(
        None,
        description='Number of pallets that follow the European standard, i.e. marked as something like EUR or EPAL. If not explicitly mentioned, set to 0.',
        title='Number Eur Pallet',
    )
    observation: Optional[str] = Field(
        None,
        description='Information about goods, packing, and handling requirements. This includes:\n\t•\tReference numbers (e.g., product codes, serial numbers)\n\t•\tHandling instructions, stacking limits, and loading specs (e.g., side/rear-loading)\n\t•\tVehicle, equipment, or packaging needs\n\t•\tSpecial care (e.g., temperature control, fragility, safety warnings)\n\t•\tLabels, placards, seal/container numbers, or other markings\nWhen you write observations, write them in the same language as the email.',
        title='Observation',
    )


class PickupDatetimeData(BaseModel):
    date: Optional[date] = Field(
        None,
        description='Date of the pickup. ISO 8601 Date Format: YYYY-MM-DD',
        title='Date',
    )
    start_time: Optional[time] = Field(
        None,
        description='Start time of the pickup. ISO 8601 Time Format: hh:mm',
        title='Start Time',
    )
    end_time: Optional[time] = Field(
        None,
        description='End time of the pickup. ISO 8601 Time Format: hh:mm. Must be greater than or equal to the start_time.',
        title='End Time',
    )


class RecipientData(BaseModel):
    company_name: Optional[str] = Field(None, description='Name of the company.', title='Company Name')
    address: Optional[AddressDataSimple] = Field(
        default_factory=lambda: AddressDataSimple.parse_obj(
            {
                'city': None,
                'postal_code': None,
                'country': None,
                'line1': None,
                'line2': None,
            }
        ),
        description='Address of the recipient.',
    )
    phone_number: Optional[str] = Field(None, description='Phone number of the recipient.', title='Phone Number')
    email_address: Optional[EmailStr] = Field(None, description='Email address of the recipient.', title='Email Address')
    delivery_datetime: Optional[DeliveryDatetimeData] = Field(
        default_factory=lambda: DeliveryDatetimeData.parse_obj({'date': None, 'start_time': None, 'end_time': None}),
        description='delivery date and time. Must be after the pickup date and time.',
    )
    observations: Optional[str] = Field(
        None,
        description='Include all relevant delivery information. This includes:\n\t•\tReference numbers (e.g., delivery refs, order numbers)\n\t•\tContact details (e.g., names, roles, extensions)\n\t•\tDock/door numbers, access codes, and specific entrance instructions\n\t•\tRequired documentation and any special equipment needs\n\t•\tUnloading bay specs, timing preferences, and site access instructions\n\t•\tParking info, unloading procedures, safety protocols, and any additional notes near recipient info\nWhen you write observations, write them in the same language as the email and the documents. If they are in French, write them in French, if they are in English, write them in English.',
        title='Observations',
    )


class SenderData(BaseModel):
    company_name: Optional[str] = Field(None, description='Name of the company.', title='Company Name')
    address: Optional[AddressDataSimple] = Field(
        default_factory=lambda: AddressDataSimple.parse_obj(
            {
                'city': None,
                'postal_code': None,
                'country': None,
                'line1': None,
                'line2': None,
            }
        ),
        description='Address of the sender.',
    )
    phone_number: Optional[str] = Field(None, description='Phone number of the sender.', title='Phone Number')
    email_address: Optional[EmailStr] = Field(None, description='Email address of the sender.', title='Email Address')
    pickup_datetime: Optional[PickupDatetimeData] = Field(
        default_factory=lambda: PickupDatetimeData.parse_obj({'date': None, 'start_time': None, 'end_time': None}),
        description='pickup date and time.',
    )
    observations: Optional[str] = Field(
        None,
        description='Include all relevant information for pickup and sender details. This includes:\n\t•\tReference numbers (e.g., order or booking refs)\n\t•\tContact details (e.g., names, roles, extensions)\n\t•\tDock/door numbers, access codes, and navigation instructions\n\t•\tRequired documentation and special equipment needs\n\t•\tLoading bay specs, timing preferences, and site access instructions\n\t•\tParking info, specific entrance locations, and any additional sender notes\nWhen you write observations, write them in the same language as the email and the documents. If they are in French, write them in French, if they are in English, write them in English.',
        title='Observations',
    )


class Category(Enum):
    Dry = 'Dry'
    Fresh = 'Fresh'
    Frozen = 'Frozen'


class TemperatureInfosData(BaseModel):
    min_temperature: Optional[float] = Field(None, description='Minimum temperature (in Celsius)', title='Min Temperature')
    max_temperature: Optional[float] = Field(None, description='Maximum temperature (in Celsius)', title='Max Temperature')
    category: Optional[Category] = Field(None, description='Temperature control requirements', title='Category')


class TransportPriceData(BaseModel):
    total_price: Optional[float] = Field(
        None,
        description='Net price of the booking order (excluding taxes)',
        title='Total Price',
    )
    currency: Optional[str] = Field(None, description='Three-letter currency code (ISO 4217).', title='Currency')


class VehicleType(Enum):
    Tractor = 'Tractor'
    Carrier = 'Carrier'
    Light_Vehicle = 'Light Vehicle'


class BodyType(Enum):
    Tautliner = 'Tautliner'
    Dry_Van = 'Dry Van'
    Refrigerated = 'Refrigerated'
    Flatbed = 'Flatbed'
    Tanker = 'Tanker'


class TruckData(BaseModel):
    thinking: Optional[str] = Field(
        None,
        description="Document the specific facts from the source that determine vehicle requirements. For example:\n- List any explicitly mentioned vehicle specifications\n- Note any temperature requirements stated\n- Record loading/unloading equipment mentioned\n- Include any access restrictions specified\n\nExample: 'Source specifies: refrigerated transport required, -20°C, loading dock not available, tail lift needed.'\n\nOnly include information that is explicitly stated in the source document. Do not make assumptions about requirements that aren't clearly specified.",
        title='Thinking',
    )
    vehicle_type: Optional[VehicleType] = Field(
        None,
        description="Primary vehicle classification:\n- 'Tractor': for semi-trailer trucks (Tracteur)\n- 'Carrier': for rigid trucks (Porteur) \n- 'Light Vehicle': for vans and smaller commercial vehicles (Véhicule léger)",
        title='Vehicle Type',
    )
    body_type: Optional[BodyType] = Field(
        None,
        description="Type of cargo body/trailer:\n- 'Tautliner': curtainside trailer (Tautliner/Transpalette)\n- 'Dry Van': box trailer (Fourgon)\n- 'Refrigerated': temperature-controlled (Réfrigéré)\n- 'Flatbed': open platform (Plateau)\n- 'Tanker': liquid cargo (Citerne)",
        title='Body Type',
    )
    tail_lift: Optional[bool] = Field(
        None,
        description='Indicates if the vehicle is equipped with a hydraulic tail lift for ground-level loading/unloading without dock access (Hayon élévateur)',
        title='Tail Lift',
    )
    crane: Optional[bool] = Field(
        None,
        description='Indicates if the vehicle is equipped with a loading crane/HIAB for self-loading and unloading of heavy cargo (Grue)',
        title='Crane',
    )


class GoodsData(BaseModel):
    thinking: Optional[str] = Field(
        None,
        description='Document your analysis of the goods information from the source document. Include:\n\n1. Description of what\'s being transported\n2. Any reference numbers or codes found\n3. Special handling requirements\n4. Equipment needs\n5. Safety considerations\n6. Documentation requirements\n7. The presence of returnable Euro pallets (it has to be explicitly stated that the pallets are EU pallets in the source document in the sender section (not in the legal mentions))\n\nExample: "Source indicates: \n- 12 pallets of automotive parts\n- Reference: ORDER123, BATCH456\n- Requires forklift for unloading\n- Non-stackable items\n- Fragile goods warning labels needed"\n- Weight is in displayed in tons - A conversion to kg is needed\n\nList all relevant details found in the source document. Do not make assumptions about information that isn\'t explicitly stated.',
        title='Thinking',
    )
    packing: Optional[PackingData] = Field(
        default_factory=lambda: PackingData.parse_obj(
            {
                'units': None,
                'packing_type': None,
                'supplementary_parcels': None,
                'pallets_on_ground': None,
                'number_eur_pallet': None,
                'observation': None,
            }
        ),
        description='Packing details of the good',
    )
    dimensions: Optional[DimensionsData] = Field(
        default_factory=lambda: DimensionsData.parse_obj({'loading_meters': None, 'volume': None}),
        description='Dimensions of the good',
    )
    weight: Optional[float] = Field(None, description='Weight of the good (in kilograms)', title='Weight')
    temperature_infos: Optional[TemperatureInfosData] = Field(
        {'min_temperature': None, 'max_temperature': None, 'category': None},
        description='Temperature infos of the good',
    )
    dangerous_goods_infos: Optional[List[DangerousGoodsInfoData]] = Field(
        [],
        description='Dangerous goods infos of the good',
        title='Dangerous Goods Infos',
    )


class ShipmentData(BaseModel):
    thinking: Optional[str] = Field(
        None,
        description='Document your analysis of the shipment information. Include:\n\n1. How you identified this as a distinct shipment\n2. Key reference numbers and their sources\n3. Relationships between pickup and delivery points\n4. Any special routing or timing requirements\n5. Document references (CMR, waybills, etc.)\n\nExample: "Source shows:\n- Single shipment identified by CMR #12345\n- Pickup from warehouse A to delivery point B\n- Must deliver within 24h window\n- References found: Order #789, Customer PO #456"\n\nDocument your reasoning process and any key decisions made in interpreting the shipment structure.',
        title='Thinking',
    )
    shipment_id: Optional[str] = Field(
        None,
        description='Unique identifier for the shipment, most often the CMR number or CMR reference, used for tracking and documenting transport details. Can also be client / sender reference number. If several numbers are provided and the situation is ambiguous, pick the most logical one, and put other numbers in the observation field.',
        title='Shipment Id',
    )
    sender: Optional[SenderData] = Field(
        default_factory=lambda: SenderData.parse_obj(
            {
                'company_name': None,
                'address': {
                    'city': None,
                    'country': None,
                    'line1': None,
                    'line2': None,
                    'postal_code': None,
                },
                'phone_number': None,
                'email_address': None,
                'pickup_datetime': {'date': None, 'end_time': None, 'start_time': None},
                'observations': None,
            }
        ),
        description='Sender data',
    )
    recipient: Optional[RecipientData] = Field(
        default_factory=lambda: RecipientData.parse_obj(
            {
                'company_name': None,
                'address': {
                    'city': None,
                    'country': None,
                    'line1': None,
                    'line2': None,
                    'postal_code': None,
                },
                'phone_number': None,
                'email_address': None,
                'delivery_datetime': {
                    'date': None,
                    'end_time': None,
                    'start_time': None,
                },
                'observations': None,
            }
        ),
        description='Recipient data',
    )
    goods: Optional[GoodsData] = Field(
        default_factory=lambda: GoodsData.parse_obj(
            {
                'packing': {
                    'number_eur_pallet': None,
                    'observation': None,
                    'packing_type': None,
                    'pallets_on_ground': None,
                    'supplementary_parcels': None,
                    'units': None,
                },
                'dimensions': {'loading_meters': None, 'volume': None},
                'weight': None,
                'temperature_infos': {
                    'category': None,
                    'max_temperature': None,
                    'min_temperature': None,
                },
                'dangerous_goods_infos': [],
            }
        ),
        description='Description of transported goods',
    )
    transport_constraints: Optional[TruckData] = Field(
        default_factory=lambda: TruckData.parse_obj({'vehicle_type': None, 'body_type': None, 'tail_lift': None, 'crane': None}),
        description='List of transport constraints informations',
    )


class RoadBookingConfirmationData(BaseModel):
    shipment_thinking: Optional[str] = Field(
        None,
        description='Document your analysis for each shipment. For each shipment identified in the document, include:\n\n1. A detailed description of the goods being transported, including any reference numbers, dangerous goods information, and packing details.\n2. The sender’s information, including the company name, address, contact details, and any relevant observations about the pickup process.\n3. The recipient’s information, including the company name, address, contact details, and any relevant observations about the delivery process.\n4. Any trucking constraints, including vehicle requirements, loading/unloading equipment, and specific transport conditions.\n\nExample:\n"Shipment Analysis:\n- Shipment 1:\n  - Goods: 4 EUR pallets containing fragrance products (UN 3082, liquid, 9, GE III), 500kg.\n  - Sender: Aroma Factory Lyon, 14 Avenue des Arômes, Lyon. Contact: +33 4 78 12 34 56. Pickup date: 31/10/2023. Observations: \'Side-loading required.\'\n  - Recipient: Perfume Retailer Nantes, 7 Rue des Fleurs, Nantes. Contact: florent.bisson@example.com, +33 2 40 12 34 78. Delivery date: 06/11/2023. Observations: \'Forklift required.\'\n  - Trucking Constraints: Refrigerated vehicle (-20°C), tail lift needed, curtainside body type.\n\n- Shipment 2:\n  - Goods: 1.5 pallets of liquid extracts (UN 1197, aromatic liquid, 3, GE III), 20kg.\n  - Sender: Logistics Hub Marseille, 28 Rue des Ports, Marseille. Contact: +33 4 91 56 78 90. Pickup date: 31/10/2023. Observations: \'Access restricted; contact for gate code.\'\n  - Recipient: Retailer Aux Arômes, 12 Avenue des Champs, Bordeaux. Contact: nadege.d@example.com, +33 5 56 78 90 12. Delivery date: 06/11/2023. Observations: \'Loading dock available.\'\n  - Trucking Constraints: Light vehicle required, no tail lift, flatbed body type.\n\n- Shipment 3:\n  - Goods: 2 custom pallets of specialty chemicals (UN 3077, solid, 9, GE III), 150kg.\n  - Sender: Industrial Park Lille, 10 Rue des Usines, Lille. Contact: +33 3 20 45 67 89. Pickup date: 01/11/2023. Observations: \'Loading requires crane.\'\n  - Recipient: ChemCo Distribution, 44 Avenue de l\'Industrie, Rouen. Contact: +33 2 32 67 89 10, logistics@chemco.com. Delivery date: 07/11/2023. Observations: \'Fragile goods, stacking not allowed.\'\n  - Trucking Constraints: Specialized vehicle with crane, dry van body type."\n\nEnsure that each shipment is clearly detailed with all relevant information. Do not omit any critical details.',
        title='Shipment Thinking',
    )
    thinking: Optional[str] = Field(
        None,
        description='Document your analysis of the overall booking confirmation. Include:\n\n1. Document type identification and confidence\n2. Key parties involved (client, carrier, etc.)\n3. Overall structure of the shipments\n4. Critical booking details and requirements\n5. Any ambiguities or unclear elements\n\nExample: "Analysis shows:\n- Clear booking confirmation document from ABC Corp\n- Contains 2 distinct shipments under single booking reference\n- Client identified as ABC Corp from letterhead\n- Total value and payment terms clearly stated\n- All required signatures present"\n\nExplain your reasoning for key decisions made in interpreting the document structure.',
        title='Thinking',
    )
    booking_id: Optional[str] = Field(
        None,
        description='Unique identifier for the booking used for billing reference',
        title='Booking Id',
    )
    payment: TransportPriceData = Field(..., description='Payment data')
    client: ClientData = Field(..., description='Client data used for billing')
    number_of_shipments: Optional[int] = Field(
        None,
        description='Number of shipments in the booking. Most frequently 1, but can be 2,3 to 10-20',
        title='Number Of Shipments',
    )
    shipments_thinking: Optional[str] = Field(
        None,
        description='Document your analysis for each shipment. For each shipment identified in the document, include:\n\n1. A detailed description of the goods being transported, including any reference numbers, dangerous goods information, and packing details.\n2. The sender’s information, including the company name, address, contact details, and any relevant observations about the pickup process.\n3. The recipient’s information, including the company name, address, contact details, and any relevant observations about the delivery process.\n4. Any trucking constraints, including vehicle requirements, loading/unloading equipment, and specific transport conditions.\n\nExample:\n"Shipment Analysis:\n1: SSP BOC - 4 EUR pallets, 10ML, 7,623 kg  (UN 3082, liquid, 9, GE III)\n2: AMC(31) BOS 2249 - 8 pallets, 7ML, 3,240 kg\n3: VETISOL BOS 2195 - 10 pallets, 9ML, 3,780 kg\n4: VETISOL BOS 2282 - 6 pallets, 5ML, 2,020 kg\n5: SOERMEL BOS 2264 - 2 pallets, 8ML, 1,300 kg (UN 3077, solid, 9, GE III)\n6: DUMOULIN BOS 2281 - 15 pallets, 11ML, 10,400 kg\n7: SOLUSTIL BOS 1764 - 20 pallets, 12ML, 24,800 kg Refrigerated vehicle (-20°C)\n8: TECMA TAR 323 - 1 pallet, 2ML, 1,475 kg\n9: PAILLET BOS 2290 - 8 pallets, 10ML, 4,945 kg\n\nEnsure that each shipment is clearly detailed with all relevant information. Do not omit any critical details.\nMost frequently, there is going to be one or two shipments in the document, but sometimes you can have a massive number of shipments on several lines, more like a table containing a long list of shipments.\nIn this case, you should create a shipment for each line of the table, it can go to 10-20 shipments sometimes.\n',
        title='Shipments Thinking',
    )
    shipments: List[ShipmentData] = Field(
        ...,
        description='List of shipment data. The number of entries should correspond to the total loading/delivery point combinations identified in the document.',
        title='Shipments',
    )
