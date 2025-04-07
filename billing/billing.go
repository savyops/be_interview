package main

import (
	"errors"
	"fmt"
	"time"
)

type Subscription struct {
	UserID    string
	Plan      string // "monthly" or "yearly"
	StartDate time.Time
	EndDate   time.Time
	Status    string // "active", "expired", "payment_failed"
}

var ErrPaymentFailed = errors.New("payment failed")


// ChargeUser simulates a payment charge (mock for interview).
func ChargeUser(userID string, amount float64) error {
	// Simulate occasional failures. 20% failure rate for testing
	if time.Now().Second()%5 == 0 { 
		return ErrPaymentFailed
	}

	// In a real system, call Stripe/PayPal/etc.
	fmt.Printf("Charged %s $%.2f\n", userID, amount)
	return nil // Assume success for now
}


func CreateSubscription(userID, plan string) (*Subscription, error) {
	sub := &Subscription{
		UserID:    userID,
		Plan:      plan,
		StartDate: time.Now(),
		Status:    "active",
	}

	duration := 30 * 24 * time.Hour // Default: monthly
	if plan == "yearly" {
		duration = 365 * 24 * time.Hour
	}
	sub.EndDate = sub.StartDate.Add(duration)

	err := ChargeUser(userID, 10.0) // Flat fee for simplicity
	if err != nil {
		return nil, err
	}
	return sub, nil
}

func main() {
	sub, _ := CreateSubscription("user123", "monthly")
	fmt.Printf("Subscription: %+v\n", sub)
}
