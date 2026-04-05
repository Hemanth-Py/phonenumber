# phonenumber

Areeba payment gateway integration — session initiation and checkout flow.

---

## What It Does

- `create_order.py` — Initiates a checkout session via the Areeba REST API (INITIATE_CHECKOUT)
- `index.html` — Hosted checkout page
- `payments.html` — Payment status/result page

Uses Basic auth with merchant credentials to create order sessions.

---

## Tech Stack

- Python 3 (standard library only)
- Areeba Payment Gateway API

---

## Setup

```bash
git clone https://github.com/Hemanth-Py/phonenumber.git
cd phonenumber

cp .env.example .env
# Edit .env with your Areeba merchant credentials
```

## Run

```bash
python create_order.py
```

---

## Environment Variables

```bash
AREEBA_MERCHANT_ID=your-merchant-id
AREEBA_PASSWORD=your-api-password
```

---

**Built with:** Python · Areeba Payment Gateway
