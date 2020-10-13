using UnityEngine;
using System;
using System.Linq;
using Assets.LSL4Unity.Scripts.AbstractInlets;

namespace Assets.LSL4Unity.Scripts.Examples
{
    /// <summary>
    /// Just an example implementation for a Inlet recieving float values
    /// </summary>
    public class ExampleFloatInlet : AFloatInlet
    {
        public string lastSample = String.Empty;

        protected override void Process(float[] newSample, double timeStamp)
        {
            // just as an example, make a string out of all channel values of this sample
            lastSample = string.Join(" ", newSample.Select(c => c.ToString()).ToArray());

            Debug.Log(newSample[0]);
            float emg = newSample[0];

            Vector3 lift = new Vector3(0, 0.2f + emg, 0);
            gameObject.transform.position = lift;
        }
    }
}