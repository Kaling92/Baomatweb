package edu.example.a11ylab

import android.app.Activity
import android.os.Bundle
import android.view.ViewGroup
import android.widget.Button
import android.widget.CheckBox
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val layout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(32, 32, 32, 32)
        }
        val title = TextView(this).apply {
            text = "Accessibility observer lab"
            textSize = 22f
        }
        val explanation = TextView(this).apply {
            text = "Use only synthetic values here. The observer records structural node counts, not displayed text."
        }
        val sampleInput = EditText(this).apply {
            hint = "Synthetic test input only"
            contentDescription = "Synthetic lab input"
        }
        val sampleCheckBox = CheckBox(this).apply {
            text = "Sample UI control"
        }
        val status = TextView(this).apply {
            text = "No lab action performed."
        }
        val sampleButton = Button(this).apply {
            text = "Update lab status"
            setOnClickListener {
                status.text = "The lab button was activated."
            }
        }
        layout.addView(title)
        layout.addView(explanation)
        layout.addView(
            sampleInput,
            ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
            )
        )
        layout.addView(sampleCheckBox)
        layout.addView(sampleButton)
        layout.addView(status)
        setContentView(layout)
    }
}
