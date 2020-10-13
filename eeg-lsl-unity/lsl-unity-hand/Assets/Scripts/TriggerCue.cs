using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerCue : MonoBehaviour
{
    public Animator HandLeft;

    float trialTime = 4;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("left"))
        {
            Debug.Log("trigger");
            HandLeft.SetTrigger("Grasp");
            StartCoroutine(ResetHands());

        }
        
    }
    IEnumerator ResetHands()
    {
        yield return new WaitForSeconds(trialTime);
        HandLeft.SetTrigger("Idle");
    }
}
