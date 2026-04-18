import sys
from creditriskengine.core.types import SAExposureClass, Jurisdiction, CreditQualityStep
from creditriskengine.rwa.standardized.credit_risk_sa import assign_sa_risk_weight

def main():
    exposure_amount = 100000.0  # 100k USD
    ltv = 0.75                  # 75% LTV

    # Calculate the SA Risk Weight
    rw_percent = assign_sa_risk_weight(
        exposure_class=SAExposureClass.RESIDENTIAL_MORTGAGE,
        cqs=CreditQualityStep.UNRATED,
        jurisdiction=Jurisdiction.BCBS,
        ltv=ltv
    )

    # Calculate the Risk Weighted Assets (RWA)
    rwa = exposure_amount * (rw_percent / 100.0)

    print(f"Exposure Amount: ${exposure_amount:,.2f}")
    print(f"Loan-to-Value (LTV): {ltv * 100:.1f}%")
    print(f"Assigned Risk Weight: {rw_percent}%")
    print(f"Calculated RWA: ${rwa:,.2f}")

if __name__ == "__main__":
    main()
