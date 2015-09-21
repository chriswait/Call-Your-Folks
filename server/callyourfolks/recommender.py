def update_user_contact_recommendation(user, contact):
    recent_call = most recent call between user & contact
    contact.next_call_date = recent_call.date + contact.period 

def update_user_contact(user, contact, call):
    user.calls_list.append(call)
    update_user_contact_recommendation(user, contact)

def get_recomendations(user):
    clear_all_recommended_calls(user)

    max_days_in_advance = 3
    max_soon_recommendations = 5
    recommendations = {
        today: [],
        soon: [],
    }

    # Get contacts with overdue calls,
    #    and contacts with calls for next few days
    for contact in user.contacts:
        # Higher diff -> more overdue
        # 1 ->  should have been yesterday
        # -1 -> should be tomorrow
        diff = today - contact.next_call_date
        if (diff >= 0):
            recommendations.today.append(contact)
        elif ((diff >= -max_days_in_advance) and len(recommendations.soon) < max_soon_recommendations):
            recommendations.soon.append(contact)

    # Sort recommendations by urgency, prioritising calls
    # * that are more overdue (with higher diff)
    # * for contacts with shorter periods
    

    return recommendations
