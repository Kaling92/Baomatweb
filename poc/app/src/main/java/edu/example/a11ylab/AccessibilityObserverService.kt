package edu.example.a11ylab

import android.accessibilityservice.AccessibilityService
import android.util.Log
import android.view.accessibility.AccessibilityEvent
import android.view.accessibility.AccessibilityNodeInfo

class AccessibilityObserverService : AccessibilityService() {
    override fun onAccessibilityEvent(event: AccessibilityEvent?) {
        event ?: return
        if (event.packageName?.toString() != packageName) return

        val root = rootInActiveWindow ?: return
        val summary = NodeSummary()
        try {
            inspectNode(root, depth = 0, summary = summary)
            Log.i(
                TAG,
                "eventType=${event.eventType} package=$packageName " +
                    "nodes=${summary.nodes} clickable=${summary.clickable} " +
                    "editable=${summary.editable} truncated=${summary.truncated}"
            )
        } finally {
            root.recycle()
        }
    }

    override fun onInterrupt() {
        Log.i(TAG, "Observer interrupted by the system.")
    }

    private fun inspectNode(
        node: AccessibilityNodeInfo,
        depth: Int,
        summary: NodeSummary
    ) {
        if (depth > MAX_DEPTH || summary.nodes >= MAX_NODES) {
            summary.truncated = true
            return
        }

        summary.nodes++
        if (node.isClickable) summary.clickable++
        if (node.isEditable) summary.editable++

        for (index in 0 until node.childCount) {
            if (summary.nodes >= MAX_NODES) {
                summary.truncated = true
                break
            }
            val child = node.getChild(index) ?: continue
            try {
                inspectNode(child, depth + 1, summary)
            } finally {
                child.recycle()
            }
        }
    }

    private class NodeSummary {
        var nodes = 0
        var clickable = 0
        var editable = 0
        var truncated = false
    }

    private companion object {
        const val TAG = "A11yObserver"
        const val MAX_DEPTH = 12
        const val MAX_NODES = 100
    }
}
